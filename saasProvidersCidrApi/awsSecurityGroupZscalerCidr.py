import boto3
import requests
from botocore.exceptions import ClientError


ec2 = boto3.client('ec2')
seperator = "\n"
count = 0
ipranges = ""
vpc_id = "vpc-########"

def create_sg(count):
    groupname = "Zscaler" + str(count+1) + "-" + str(count+50)

    try:
        response = ec2.create_security_group(GroupName=groupname,
            Description='Zscaler ZIA Nodes',
            VpcId=vpc_id)
        security_group_id = response['GroupId']
        print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))
        return security_group_id
    except ClientError as e:
        print(e)
        return False

zs_dc = requests.get("http://ips.zscaler.net/sites/default/files/geoips/geoip.csv")
zs_dc_list = zs_dc.content.decode().split(seperator)

for line in zs_dc_list:
    if "," not in line:
        continue
    if count % 50 == 0:
        security_group_id = create_sg(count)
        print ("Created new security group: " + str(security_group_id))

    dc_elements = line.split(",")
    ip_range = dc_elements[0].strip('"')
    city = dc_elements[3].strip('"')
    state = dc_elements[2].strip('"')
    country = dc_elements[1].strip('"')
    description = country + " " + state + " " + city
    print("adding rule for:" + description)

    dc_elements = {}

    try:
        data = ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {'IpProtocol': "-1",
                'IpRanges': [{'CidrIp': ip_range}]}
            ])
        print('Ingress Successfully Set %s' % data)
        count += 1
    except ClientError as e:
        print(e)
