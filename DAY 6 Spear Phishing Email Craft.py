def spear_phish_template(target):
    return f"""
============================================================
[SIMULATION EMAIL - FOR AWARENESS TRAINING ONLY]
============================================================
From    : it-support@{target['company'].lower()}-security-portal.com
To      : {target['email']}
Subject : Action Required: Your {target['company']} account will be disabled

Hi {target['name']},

Our security team noticed an unusual login attempt from {target['location']}.
Please verify your corporate account within 24 hours to avoid permanent suspension.

[ Verify Account Securely ] -> https://internal-auth.lab-sandbox.local/verify

Regards,
IT Security Team ({target['company']})
============================================================
"""

# List of targets (Simulated OSINT Data)
targets = [
    {"name": "Riya Sharma", "email": "riya@company.com", "company": "Sqrock", "location": "Bangalore, India"},
    {"name": "Amit Patil", "email": "amit@company.com", "company": "Sqrock", "location": "Mumbai, India"},
    {"name": "Priya Deshmukh", "email": "priya@company.com", "company": "Sqrock", "location": "Pune, India"}
]

# Generate and print emails for all targets
if __name__ == "__main__":
    for t in targets:
        print(spear_phish_template(t))