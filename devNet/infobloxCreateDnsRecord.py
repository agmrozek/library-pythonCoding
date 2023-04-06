import requests
import json

def create_dns_records(input_file):
    # Infoblox API endpoint URL
    url = 'https://infoblox.example.com/wapi/v2.10/'

    # Infoblox API credentials
    username = 'api_username'
    password = 'api_password'

    # Read input file
    with open(input_file, 'r') as f:
        dns_names = f.read().splitlines()

    # Loop through DNS names and create A records
    for dns_name in dns_names:
        # Build Infoblox API request body
        request_body = {
            'name': dns_name,
            'ipv4addr': '1.2.3.4'  # Replace with desired IP address
        }

        # Send Infoblox API request to create A record
        response = requests.post(url + 'record:a', auth=(username, password), json=request_body)

        # Check for errors in response
        if response.status_code != 201:
            print(f'Error creating A record for {dns_name}: {response.text}')
        else:
            print(f'Successfully created A record for {dns_name}')
