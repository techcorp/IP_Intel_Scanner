import requests
import socket
import json
import pyfiglet
from termcolor import colored

def print_banner():
    banner = pyfiglet.figlet_format("IP Intel Scanner")
    print(colored(banner, "cyan"))

def get_ip_data(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP data: {e}")
        return None

def reverse_dns_lookup(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Not Found"

def check_proxy_vpn(ip):
    try:
        proxy_api = requests.get(f"http://proxycheck.io/v2/{ip}?vpn=1")
        proxy_api.raise_for_status()
        data = proxy_api.json()
        return data.get(ip, {}).get('proxy', 'Unknown')
    except requests.exceptions.RequestException:
        return "Unknown"

def get_threat_info(ip):
    try:
        threat_api = requests.get(f"https://threatintelligence.com/api/{ip}")
        threat_api.raise_for_status()
        data = threat_api.json()
        return "Malicious" if data.get('threat', False) else "Safe"
    except requests.exceptions.RequestException:
        return "Unknown"

def main():
    print_banner()
    try:
        ip = input(colored("Enter IP address: ", "yellow"))
        api = get_ip_data(ip)
        if not api:
            print(colored("Failed to retrieve IP data.", "red"))
            return
        
        status = "Valid" if api.get('status') == "success" else "Invalid"
        country = api.get('country', "None")
        country_code = api.get('countryCode', "None")
        region = api.get('regionName', "None")
        city = api.get('city', "None")
        latitude = api.get('lat', "None")
        longitude = api.get('lon', "None")
        isp = api.get('isp', "None")
        org = api.get('org', "None")
        asn = api.get('as', "None")
        timezone = api.get('timezone', "None")
        zip_code = api.get('zip', "None")
        
        reverse_dns = reverse_dns_lookup(ip)
        proxy_status = check_proxy_vpn(ip)
        threat_status = get_threat_info(ip)
        
        print(colored(f"""
        Status       : {status}
        Country      : {country} ({country_code})
        Region       : {region}
        City         : {city}
        Latitude     : {latitude}
        Longitude    : {longitude}
        Timezone     : {timezone}
        ISP          : {isp}
        Organization : {org}
        ASN          : {asn}
        Zip Code     : {zip_code}
        Reverse DNS  : {reverse_dns}
        Proxy/VPN    : {proxy_status}
        Threat Check : {threat_status}
        Google Maps  : https://www.google.com/maps?q={latitude},{longitude}
        """, "green"))
    except Exception as e:
        print(colored(f"An unexpected error occurred: {e}", "red"))

if __name__ == "__main__":
    main()
