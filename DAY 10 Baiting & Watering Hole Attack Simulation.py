from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import json

# List to store captured victim/visitor logs
LOG = []

class HoneyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Capture details of the user who clicked the bait link
        entry = {
            "time": str(datetime.datetime.now()),
            "ip": self.client_address[0],
            "path": self.path,
            "agent": self.headers.get("User-Agent", "Unknown"),
        }
        
        LOG.append(entry)
        
        # Print the captured details to the console in readable JSON format
        print("\n[!] BAIT CLICKED! Captured Visitor Data:")
        print(json.dumps(entry, indent=2))
        
        # Send an HTTP response to the browser
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Security Awareness Training Demo Page</h1>")

    def log_message(self, format, *args):
        # Suppress standard HTTP request logging to keep output clean
        pass

def run_honeypot():
    port = 8080
    print(f"==================================================")
    print(f"[+] Starting Honeypot Server on http://localhost:{port}")
    print(f"[+] Waiting for clicks on bait links...")
    print(f"==================================================")
    
    server = HTTPServer(("", port), HoneyHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[-] Stopping Honeypot Server...")
        server.server_close()

if __name__ == "__main__":
    run_honeypot()