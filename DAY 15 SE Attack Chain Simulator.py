import sys
import re
import json
import datetime
from collections import Counter

# ==========================================
# MODULE 1: OSINT Scanner
# ==========================================
def run_osint_scanner(domain):
    print(f"\n[+] Running Passive OSINT Reconnaissance on domain: '{domain}'...")
    
    # Simulated OSINT Recon Results (Domains, Employees, Infrastructure)
    osint_data = {
        "domain": domain,
        "mx_records": [f"mail.{domain}", f"smtp.{domain}"],
        "discovered_emails": [
            f"admin@{domain}",
            f"hr@{domain}",
            f"divya_wankhede@{domain}"
        ],
        "tech_stack": ["Microsoft 365", "Outlook Web App", "Azure AD"],
        "exposed_ports": [80, 443, 25]
    }
    
    print("✔ OSINT Gathering Complete:")
    print(f"   • Discovered Emails: {', '.join(osint_data['discovered_emails'])}")
    print(f"   • Tech Stack Detected: {', '.join(osint_data['tech_stack'])}")
    return osint_data


# ==========================================
# MODULE 2: Target Profile Builder
# ==========================================
def build_target_profile(osint_data):
    print("\n[+] Building Target Profiles from OSINT Data...")
    
    target_profiles = []
    for email in osint_data["discovered_emails"]:
        username = email.split('@')[0]
        role = "Administrator" if "admin" in username else ("HR Manager" if "hr" in username else "Employee")
        
        profile = {
            "email": email,
            "username": username,
            "role": role,
            "primary_vector": "Credential Harvesting via M365 Spoofing" if "Microsoft 365" in osint_data["tech_stack"] else "Generic Phish"
        }
        target_profiles.append(profile)
        print(f"   • Profile Created: {profile['username']} | Role: {profile['role']} | Recommended Vector: {profile['primary_vector']}")
        
    return target_profiles


# ==========================================
# MODULE 3: Phish Crafting & Generator
# ==========================================
def craft_phish_email(target_profile):
    print(f"\n[+] Crafting Phishing Email Template for '{target_profile['email']}'...")
    
    subject = "URGENT: Microsoft 365 Password Expiration Notice"
    body = f"""Dear {target_profile['username'].title()},

Your Microsoft 365 password is set to expire in 2 hours. To avoid account suspension and losing access to corporate emails, please update your credentials immediately using the secure link below:

http://login.microsoft365-verify-portal.com/auth/login?user={target_profile['email']}

If you do not update your password promptly, your account will be locked by system administration.

Regards,
IT Infrastructure Support Team
"""
    print("✔ Phishing Template Generated:")
    print("-" * 50)
    print(f"Subject: {subject}\n\n{body}")
    print("-" * 50)
    return {"subject": subject, "body": body}


# ==========================================
# MODULE 4: Phish Scorer
# ==========================================
def score_phish_email(email_payload):
    print("\n[+] Evaluating Email Phishing/Suspicion Score...")
    
    suspicious_keywords = ["urgent", "immediately", "expire", "suspension", "verify", "update", "locked", "password"]
    text = (email_payload["subject"] + " " + email_payload["body"]).lower()
    
    score = 0
    detected_indicators = []
    
    # 1. Keyword Check
    for word in suspicious_keywords:
        if word in text:
            score += 10
            detected_indicators.append(f"Urgency Keyword: '{word}'")
            
    # 2. Suspicious Link / Urgency Check
    if "http://" in text or "login." in text:
        score += 25
        detected_indicators.append("Unencrypted HTTP / Lookalike Domain Link")
        
    if "password" in text and "expire" in text:
        score += 20
        detected_indicators.append("Credential Harvesting Trigger")

    print(f"📊 Phish Score: {score}/100")
    print("   Detected Threat Indicators:")
    for ind in detected_indicators:
        print(f"     - {ind}")
        
    return score


# ==========================================
# MODULE 5: Incident Response (IR) Trigger
# ==========================================
def trigger_ir_workflow(target_profile, score):
    print("\n[+] Evaluating Incident Response (IR) Containment Triggers...")
    
    if score >= 50:
        print("🚨 THREAT THRESHOLD EXCEEDED! Triggering Automated IR Containment Workflow...")
        
        actions = [
            f"LOCK account: {target_profile['email']}",
            f"REVOKE active OAuth tokens & sessions for {target_profile['username']}",
            "QUARANTINE email payload across mail gateway",
            "BLOCK malicious domain: login.microsoft365-verify-portal.com",
            "ALERT Security Operations Center (SOC) team via PagerDuty"
        ]
        
        print("\n=== AUTOMATED CONTAINMENT ACTIONS EXECUTED ===")
        for idx, action in enumerate(actions, 1):
            print(f" {idx}. [SUCCESS] {action}")
            
        # Log incident report to JSON for compliance & auditing
        report = {
            "timestamp": str(datetime.datetime.now()),
            "target": target_profile,
            "phish_score": score,
            "actions_executed": actions
        }
        
        filename = f"se_simulation_ir_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)
        print(f"\n📁 Compliance audit record saved to: {filename}")
    else:
        print("ℹ️ Risk score below threshold. No containment action required.")


# ==========================================
# MAIN EXECUTION CONTROLLER
# ==========================================
def run_se_attack_chain():
    print("=" * 65)
    print("   🛡️  SOCIAL ENGINEERING ATTACK CHAIN SIMULATOR (ETHICAL LAB)  🛡️")
    print("=" * 65)
    
    target_domain = input("\n🌐 Enter Target Domain (e.g., company.com):\n> ").strip()
    if not target_domain:
        target_domain = "corp-example.com"
        
    # Phase 1: OSINT Reconnaissance
    osint_results = run_osint_scanner(target_domain)
    
    # Phase 2: Target Profiling
    target_profiles = build_target_profile(osint_results)
    
    # Select the first profile for attack chain simulation
    selected_target = target_profiles[2] if len(target_profiles) > 2 else target_profiles[0]
    print(f"\n🎯 Selected Simulation Target: {selected_target['email']}")
    
    # Phase 3: Phishing Email Generation
    phish_payload = craft_phish_email(selected_target)
    
    # Phase 4: Phish Scoring & Analysis
    risk_score = score_phish_email(phish_payload)
    
    # Phase 5: Automated IR Trigger
    trigger_ir_workflow(selected_target, risk_score)
    
    print("\n" + "=" * 65)
    print("  [✔] FULL SOCIAL ENGINEERING ATTACK CHAIN SIMULATION COMPLETED")
    print("=" * 65)


if __name__ == "__main__":
    run_se_attack_chain()