def generate_vishing_script(target_company, attacker_role, pretext, channel="Vishing (Voice)"):
    """Generates a structured social engineering simulation script for awareness training."""
    
    script = f"""
==================================================
[{channel.upper()}] SIMULATION SCRIPT: {pretext.upper()}
==================================================
Caller/Sender Role : {attacker_role}
Target Entity      : {target_company}
Pretext Context    : {pretext}

[1. THE HOOK / OPENER]
"Hello, this is {attacker_role} reaching out regarding an urgent security matter concerning your account with {target_company}. We've detected unusual unauthorized activity."

[2. THE PRESSURE / URGENCY]
"If we do not secure this immediately within the next 30 minutes, your account will face permanent suspension, leading to data loss and operational lockout."

[3. THE ASK (The Trap)]
"To verify your identity and restore security, please confirm your login credentials / temporary access token right now."

[4. EDUCATIONAL RED FLAGS (For Trainees)]
-> Psychological Trigger: Uses Fear, Urgency, and Authority to bypass critical thinking.
-> Red Flag 1: Legitimate IT, bank, or government entities will NEVER ask for passwords, PINs, or sensitive multi-factor authentication (MFA) codes over the phone or text.
-> Red Flag 2: Coercion through artificial deadlines ("within 30 minutes").
-> Action Required: Hang up immediately, locate the official contact number independently, and verify through legitimate internal channels.
==================================================
"""
    return script

def generate_smishing_script(attacker_role, pretext, short_link):
    """Generates an SMS phishing (smishing) template."""
    
    script = f"""
==================================================
[SMISHING (SMS)] SIMULATION SCRIPT
==================================================
Sender ID   : {attacker_role}
Message Body:
"URGENT: Your {pretext} account has been temporarily locked due to suspicious login attempts. Tap the secure link below to verify your identity immediately to avoid closure:
{short_link}"

[EDUCATIONAL RED FLAGS (For Trainees)]
-> Psychological Trigger: Fear, Scarcity, and Authority.
-> Red Flag 1: Use of generic short links or external domains instead of official branded domains.
-> Red Flag 2: Creating a false sense of panic requiring immediate action via text.
-> Action Required: Do not click the link. Log into the official app or website directly to check account status.
==================================================
"""
    return script

# --- Execution & Demonstration (3 Unique Scripts) ---

if __name__ == "__main__":
    print("--- GENERATING TRAINING SIMULATION SCRIPTS ---\n")
    
    # 1. IT Support Vishing Script
    print(generate_vishing_script(
        target_company="Sqrock IT Solutions", 
        attacker_role="Alex from Corporate IT Helpdesk", 
        pretext="Mandatory Password Reset / VPN Migration"
    ))
    
    # 2. Banking Vishing Script
    print(generate_vishing_script(
        target_company="Global Apex Bank", 
        attacker_role="Fraud Prevention Officer", 
        pretext="Unusual Credit Card Transaction Verification"
    ))
    
    # 3. Government / Tax Smishing Script
    print(generate_smishing_script(
        attacker_role="Tax Authority (Govt)", 
        pretext="Pending Tax Refund / Penalty Notice",
        short_link="https://bit.ly/gov-tax-secure-portal"
    ))