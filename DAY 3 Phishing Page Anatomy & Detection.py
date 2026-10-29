import re
from urllib.parse import urlparse

KEYWORDS = ["login", "verify", "secure", "update", "account", "bank", "paypal"]

def phish_score(url):
    p = urlparse(url)
    score = 0
    
    if not url.startswith("https"): 
        score += 30
    for kw in KEYWORDS:
        if kw in p.netloc: 
            score += 20
    if p.netloc.count('.') > 3: 
        score += 25
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', p.netloc):
        score += 40
        
    return min(score, 100)

def evaluate_url():
    # Prompt the user to enter a URL
    user_url = input("Enter a URL to check for phishing risks: ").strip()
    
    score = phish_score(user_url)
    print(f"\nAnalyzing URL: {user_url}")
    print(f"Risk Score: {score}%")
    
    # Generate recommendations based on the score
    print("Recommendation:")
    if score == 0:
        print(" [SAFE] This URL appears legitimate based on standard heuristics.")
    elif score < 50:
        print(" [MODERATE RISK] Exercise caution. Check the domain carefully before entering any credentials.")
    else:
        print(" [HIGH RISK / PHISHING DETECTED] Do NOT click this link, enter credentials, or download anything! This URL exhibits multiple high-risk indicators.")

if __name__ == "__main__":
    evaluate_url()