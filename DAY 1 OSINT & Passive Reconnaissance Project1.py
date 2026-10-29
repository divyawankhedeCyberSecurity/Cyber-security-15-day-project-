import socket
import requests
import whois  # Requires: pip install python-whois requests

def get_osint_info():
    # Prompt the user for a target domain
    domain = input("Enter the target domain (e.g., example.com): ").strip()
    
    if not domain:
        print("[-] Domain cannot be empty.")
        return

    print(f"\n[+] Gathering OSINT data for: {domain}\n" + "="*50)

    # 1. Fetch DNS Information (IP Address)
    ip_address = None
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"[INFO] Target IP Address: {ip_address}")
    except socket.gaierror:
        print("[-] Could not resolve domain to an IP address.")  

    # 2. Fetch WHOIS Details
    print("\n[WHOIS Details]:")
    try:
        w = whois.whois(domain)
        
        # Helper to handle cases where WHOIS returns a list of dates
        creation_date = w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date
        expiration_date = w.expiration_date[0] if isinstance(w.expiration_date, list) else w.expiration_date
        
        # Display key WHOIS fields cleanly
        print(f"  - Registrar: {w.registrar}")
        print(f"  - Creation Date: {creation_date}")
        print(f"  - Expiration Date: {expiration_date}")
        print(f"  - Name Servers: {w.name_servers}")
    except Exception as e:
        print(f"[-] Error fetching WHOIS data: {e}")

    # 3. Fetch IP Geolocation Details using requests
    if ip_address:
        print("\n[IP Geolocation Details]:")
        try:
            # Using ipapi.co free tier (no API key required for basic lookups)
            url = f"https://ipapi.co/{ip_address}/json/"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                geo_data = response.json()
                if "error" in geo_data:
                    print(f"[-] Geolocation API Error: {geo_data.get('reason', 'Unknown error')}")
                else:
                    print(f"  - Country: {geo_data.get('country_name')}")
                    print(f"  - Region/State: {geo_data.get('region')}")
                    print(f"  - City: {geo_data.get('city')}")
                    print(f"  - Postal Code: {geo_data.get('postal')}")
                    print(f"  - Organization/ISP: {geo_data.get('org')}")
            else:
                print(f"[-] Failed to fetch geolocation data. HTTP Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[-] Request error: {e}")
    else:
        print("\n[-] Skipping geolocation lookup as IP address could not be resolved.")

    print("\n" + "="*50)
    print("[+] OSINT scan completed.")

if __name__ == "__main__":
    get_osint_info()