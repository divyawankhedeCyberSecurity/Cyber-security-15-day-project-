import requests
import json

def github_profile(username):
    base = "https://api.github.com"
    
    print(f"[*] Fetching public data for GitHub user: {username}...")
    
    # Fetch basic user data
    user_response = requests.get(f"{base}/users/{username}")
    if user_response.status_code != 200:
        print(f"[!] Error: User '{username}' not found or API rate limit reached.")
        return
    
    u = user_response.json()
    
    # Fetch user repositories
    repos_response = requests.get(f"{base}/users/{username}/repos")
    repos = repos_response.json() if repos_response.status_code == 200 else []
    
    # Aggregate programming languages / tech stack
    langs = {}
    for r in repos[:10]:
        lang = r.get('language')
        if lang:
            langs[lang] = langs.get(lang, 0) + 1
            
    # Build the target threat profile
    profile = {
        "target_username": username,
        "name": u.get("name"),
        "company": u.get("company"),
        "location": u.get("location"),
        "public_repos_count": u.get("public_repos"),
        "top_tech_stack": langs,
        "bio": u.get("bio"),
        "public_profile_url": u.get("html_url")
    }
    
    # Save to JSON file
    filename = f"{username}_threat_profile.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=4)
        
    print(f"[+] Success! Profile saved locally as '{filename}'\n")
    print("--- GENERATED JSON PREVIEW ---")
    print(json.dumps(profile, indent=2))

if __name__ == "__main__":
    target_user = input("Enter GitHub username to scan (e.g., torvalds): ").strip()
    if target_user:
        github_profile(target_user)
    else:
        print("[!] Please enter a valid username.")