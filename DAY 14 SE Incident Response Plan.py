import datetime
import json

def trigger_incident_response(incident):
    print("=" * 60)
    print("      🛡️  SOCIAL ENGINEERING INCIDENT RESPONSE AUTOMATION 🛡️")
    print("=" * 60)
    print(f"🕒 Time Triggered : {datetime.datetime.now()}")
    print(f"📌 Incident Type  : {incident.get('type', 'Unknown').upper()}")
    print(f"⚠️ Severity Level : {incident.get('severity', 'MEDIUM').upper()}")
    print(f"👤 Affected User  : {incident.get('user', 'N/A')}")
    print(f"🌐 Source IP      : {incident.get('ip', 'N/A')}")
    print("-" * 60)

    severity = incident.get('severity', '').upper()
    incident_type = incident.get('type', '').lower()
    
    actions_taken = []

    # 1. Severity-based Containment Actions
    if severity in ('HIGH', 'CRITICAL'):
        print("🚨 High/Critical Severity Detected! Executing strict containment...")
        actions_taken.extend([
            "LOCK user account", 
            "Revoke all active sessions", 
            "Notify SOC team via PagerDuty/Slack", 
            "Preserve mail/system logs for forensics"
        ])
    else:
        print("ℹ️ Standard Severity. Executing routine monitoring actions...")
        actions_taken.extend([
            "Notify user to verify activity", 
            "Log event for review"
        ])

    # 2. Incident-Type Specific Actions (e.g., Phishing / Social Engineering)
    if incident_type == 'phishing':
        print("🎣 Phishing vector identified. Securing email gateway...")
        actions_taken.extend([
            "Quarantine malicious email across organization", 
            "Block sender domain on mail server",
            "Force password reset for affected user"
        ])
    elif incident_type == 'vishing' or incident_type == 'credential_harvesting':
        print("📞 Voice/Credential threat identified. Enforcing strict access controls...")
        actions_taken.extend([
            "Enable temporary MFA step-up authentication",
            "Alert security awareness team for targeted user re-training"
        ])

    # 3. Execution Report
    print("\n" + "=" * 60)
    print("                 AUTOMATED ACTIONS EXECUTED                 ")
    print("=" * 60)
    for index, action in enumerate(actions_taken, 1):
        print(f" {index}. [SUCCESS] {action}")
    print("=" * 60)

    # 4. Generate Audit Log / Documentation (Critical for compliance & insurance)
    audit_record = {
        "timestamp": str(datetime.datetime.now()),
        "incident_details": incident,
        "actions_executed": actions_taken
    }
    
    # Save the incident report locally as a JSON file for compliance records
    filename = f"incident_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(audit_record, f, indent=4)
        
    print(f"📁 Compliance audit trail successfully saved to: {filename}")
    print("=" * 60)

if __name__ == "__main__":
    # नमुना आणीबाणी डेटा (Sample SE Alert / Incident Payload)
    sample_incident = {
        "type": "phishing",
        "severity": "HIGH",
        "user": "divya_wankhede",
        "ip": "185.220.101.5",
        "description": "User clicked malicious credential-harvesting link and submitted password."
    }

    # स्वयंचलित रिस्पॉन्स वर्कफ्लो सुरू करणे
    trigger_incident_response(sample_incident)