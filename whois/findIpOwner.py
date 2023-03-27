import ipwhois
from pprint import pprint


def get_whois_info():
    ip_address = input("Enter an IP address: ")
    obj = ipwhois.IPWhois(ip_address)
    results = obj.lookup_rdap()
    pprint(results)

if __name__ == "__main__":
    get_whois_info()

