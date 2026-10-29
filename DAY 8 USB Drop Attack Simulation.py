import platform
import socket
import getpass
import os
from datetime import datetime

def collect_system_info():
    """Gathers basic non-sensitive environment data to simulate payload execution."""
    info = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Username": getpass.getuser(),
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "Operating System": platform.system(),
        "OS Release": platform.release(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "Current Directory": os.getcwd()
    }
    return info

def main():
    print("[*] Initializing simulation sequence...")
    system_data = collect_system_info()
    
    print("\n[+] Captured Telemetry Data:")
    for key, value in system_data.items():
        print(f"    - {key}: {value}")
        
    print("\n[*] Simulation complete. No persistent changes were made.")

if __name__ == "__main__":
    main()