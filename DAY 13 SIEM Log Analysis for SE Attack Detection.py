import re
from collections import Counter

def analyze_siem_logs(file_path):
    print("=" * 60)
    print("   🛡️  SIEM LOG ANALYSIS FOR SOCIAL ENGINEERING DETECTION  🛡️")
    print("=" * 60)
    
    try:
        # Open and read the log file provided by the user
        with open(file_path, 'r', encoding='utf-8') as file:
            log_data = file.readlines()
    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found. Please check the path.")
        return
    except Exception as e:
        print(f"❌ An error occurred while reading the file: {e}")
        return

    failed_attempts = Counter()
    anomaly_found = False
    
    for line in log_data:
        line = line.strip()
        if not line:
            continue
            
        # Regex to match the log format:
        # Format: YYYY-MM-DD HH:MM:SS ACTION user=NAME ip=IP [rule=RULE]
        match = re.search(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) user=(\w+) ip=([\d\.]+)(?: rule=(\w+))?", line)
        
        if not match:
            continue
            
        date, time_str, action, user, ip, rule = match.groups()
        hour = int(time_str.split(":")[0])
        
        # 1. Check for unusual login times (e.g., between midnight and 6 AM)
        if 0 <= hour < 6 and action == "SUCCESS_LOGIN":
            print(f"🚨 [ANOMALY DETECTED] Unusual Login Time!")
            print(f"   User '{user}' successfully logged in at {time_str} from IP {ip}\n")
            anomaly_found = True
            
        # 2. Check if a suspicious email forwarding rule was created
        if action == "EMAIL_RULE_CREATED":
            print(f"🚨 [SECURITY ALERT] Suspicious Email Rule Created!")
            print(f"   User '{user}' created a rule ('{rule}') at {time_str}\n")
            anomaly_found = True
            
        # 3. Track failed login attempts for brute-force detection
        if action == "FAILED_LOGIN":
            failed_attempts[(user, ip)] += 1

    # Check for brute-force or repeated failed login attempts (3 or more)
    print("-" * 60)
    print("Analyzing Brute-Force / Repeated Failed Attempts:")
    print("-" * 60)
    
    for (user, ip), count in failed_attempts.items():
        if count >= 3:
            print(f"⚠️ [WARNING] Potential Brute-Force Attack on User '{user}'")
            print(f"   From IP: {ip} | Failed Attempts: {count}\n")
            anomaly_found = True
        else:
            print(f"ℹ️ User '{user}' (IP: {ip}): {count} failed attempt(s).")
            
    if not anomaly_found:
        print("\n✅ No critical anomalies or suspicious activities detected.")
        
    print("=" * 60)
    print("Log analysis completed successfully.")
    print("=" * 60)

if __name__ == "__main__":
    # Ask the user to input the full path of their log file
    path = input("📁 Enter the full path to your log file:\n> ").strip()
    
    # Remove any accidental quotation marks around the path
    path = path.strip('"').strip("'")
    
    analyze_siem_logs(path)