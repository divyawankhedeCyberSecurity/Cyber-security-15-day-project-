import re
import requests
from bs4 import BeautifulSoup

def scrape_emails(domain):
    # Normalize domain input into a full URL
    if not domain.startswith(('http://', 'https://')):
        target_url = f"https://{domain}"
    else:
        target_url = domain

    print(f"\n[+] Target URL: {target_url}")
    print("[+] Scanning target page for email addresses...")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }

    discovered_emails = set()

    try:
        response = requests.get(target_url, headers=headers, timeout=10)
        response.raise_for_status()

        # 1. Regex search across raw HTML content for email pattern
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        found_in_text = re.findall(email_pattern, response.text)
        for email in found_in_text:
            discovered_emails.add(email.lower())

        # 2. Check anchor 'mailto:' tags specifically using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if href.startswith('mailto:'):
                email = href.replace('mailto:', '').split('?')[0].strip()
                if email:
                    discovered_emails.add(email.lower())

    except requests.exceptions.RequestException as e:
        print(f"[-] Error connecting to target webpage: {e}")
        return []

    return list(discovered_emails)

def display_pretexting_exercise(emails, domain):
    print("\n" + "="*60)
    print(" 🎯 SOCIAL ENGINEERING & PRETEXTING PREPARATION EXERCISE")
    print("="*60)
    
    if not emails:
        print("[-] No email addresses found directly on the main landing page.")
        print("[*] Note: Deeper subpages (like /contact, /about, /team) often contain public contact details.")
        return

    print(f"[+] Total Unique Emails Discovered: {len(emails)}\n")
    print("Discovered Contact Endpoints:")
    for email in emails:
        print(f"  - {email}")

    print("\n--- Pretexting Concept Mapping for Security Awareness ---")
    
    # Simple naming style heuristic
    naming_convention = "Standard / Mixed"
    for email in emails:
        local_part = email.split('@')[0]
        if '.' in local_part:
            naming_convention = "First.Last (e.g., jane.doe@...)"
            break
        elif '_' in local_part:
            naming_convention = "First_Last (e.g., jane_doe@...)"
            break

    print(f"• **Inferred Format Pattern:** {naming_convention}")
    
    print("\n• **Suggested Pretext Scenarios for Training Modules:**")
    print("  1. **IT Security Verification Pretext:**")
    print(f"     - *Scenario:* A mock notification regarding a mandatory multi-factor authentication (MFA) reset or software update for {domain} employees.")
    print("     - *Objective:* Train staff to verify IT requests through internal out-of-band channels rather than clicking links.")
    
    print("  2. **Vendor Policy Update Pretext:**")
    print(f"     - *Scenario:* An urgent alert from a common service provider or third-party vendor associated with {domain}.")
    print("     - *Objective:* Measure organization readiness against credential harvesting via third-party simulations.")
    
    print("="*60)

def main():
    print("=== Authorized OSINT Email Harvester & Pretexting Prep Tool ===")
    domain_input = input("Enter target domain or website URL: ").strip()
    
    if not domain_input:
        print("[-] Error: Input cannot be empty.")
        return

    emails = scrape_emails(domain_input)
    display_pretexting_exercise(emails, domain_input)

if __name__ == "__main__":
    main()