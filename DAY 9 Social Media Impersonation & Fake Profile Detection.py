def fake_profile_score(profile):
    score = 0
    
    # 1. नवीन अकाऊंट (Account Age)
    age_days = profile.get("account_age_days", 365)
    if age_days < 30:
        score += 30
        
    # 2. फॉलोअर्स आणि फॉलोविंग रेशो (Follower to Following Ratio)
    followers = profile.get("followers", 1)
    following = profile.get("following", 1)
    ratio = following / max(followers, 1)
    if ratio > 10:
        score += 25
        
    # 3. प्रोफाईल फोटो नसणे (No Profile Pic)
    if profile.get("no_profile_pic"):
        score += 20
        
    # 4. कमी पोस्ट्स असणे (Low Activity/Posts)
    if profile.get("posts", 100) < 5:
        score += 15
        
    # 5. डीफॉल्ट बायो (Default/Empty Bio)
    if profile.get("default_bio"):
        score += 10
        
    return min(score, 100)

def main():
    print("=== SOCIAL MEDIA FAKE PROFILE DETECTOR ===")
    
    # युझरकडून इनपुट घेणे
    platform = input("Enter Social Media Platform (e.g., Twitter/X, Instagram, LinkedIn): ").strip()
    username = input("Enter User Account / Handle to test (e.g., @john_doe_99): ").strip()
    
    print(f"\nEvaluating profile for [{username}] on [{platform}]...\n")
    
    # टेस्ट करण्यासाठी सॅम्पल प्रोफाइल डेटा (हा खरा डेटा किंवा युझर डेटा असू शकतो)
    sample_profiles = [
        {
            "account_age_days": 7,
            "followers": 2,
            "following": 900,
            "no_profile_pic": True,
            "posts": 1,
            "default_bio": True
        },
        {
            "account_age_days": 1200,
            "followers": 4500,
            "following": 320,
            "no_profile_pic": False,
            "posts": 870,
            "default_bio": False
        }
    ]

    # पहिल्या सॅम्पल प्रोफाइलचा स्कोअर काढणे
    test_profile = sample_profiles[0] # सॅम्पल संशयास्पद प्रोफाइल
    risk_score = fake_profile_score(test_profile)
    
    print("--- EVALUATION RESULT ---")
    print(f"Platform     : {platform}")
    print(f"Account Name : {username}")
    print(f"Fake Score   : {risk_score}%")
    
    if risk_score >= 60:
        print("Status       : HIGH RISK (Likely a Bot or Fake Profile)")
    elif risk_score >= 30:
        print("Status       : MEDIUM RISK (Suspicious Indicators)")
    else:
        print("Status       : LOW RISK (Appears Genuine)")

if __name__ == "__main__":
    main()