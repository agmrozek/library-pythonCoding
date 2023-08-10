#!/usr/bin/env python

import ipwhois

def extract_bgp_asn(file_path):
    with open(file_path, 'r') as f:
        ip_addresses = f.readlines()

    for ip_address in ip_addresses:
        ip_address = ip_address.strip()
        obj = ipwhois.IPWhois(ip_address)
        results = obj.lookup_rdap()
        if 'asn' in results['network']:
            bgp_asn = results['network']['asn']
            print(f"{ip_address}: {bgp_asn}")
        else:
            print(f"{ip_address}: No BGP ASN found")

file_path = "iplist.txt"

if __name__ == "__main__":
    extract_bgp_asn(file_path)
