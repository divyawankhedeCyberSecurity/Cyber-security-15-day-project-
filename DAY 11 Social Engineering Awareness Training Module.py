import sys
import time

def print_slow(text, delay=0.03):
    """Prints text with a typewriter effect for better engagement."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def run_quiz():
    # List of dictionaries containing the questions, options, correct answers, and explanations
    questions = [
        {
            "q": "An email appears to come from your IT department asking you to urgently verify your password via an external link. You should:",
            "opts": [
                "A) Click the link and enter your credentials immediately.",
                "B) Call IT directly or check through official internal channels.",
                "C) Reply to the email asking for clarification."
            ],
            "ans": "B",
            "exp": "Always verify via official internal channels. Attackers frequently impersonate IT to induce panic and urgency."
        },
        {
            "q": "You find an unknown USB flash drive labeled 'Salary Structure 2026' in the office parking lot. The safest course of action is:",
            "opts": [
                "A) Plug it into your work laptop to find the owner.",
                "B) Plug it into a personal computer to check its contents safely.",
                "C) Hand it over to the IT Security department without plugging it in."
            ],
            "ans": "C",
            "exp": "Dropped media is a classic social engineering tactic (USB drop attack) designed to infect systems with malware instantly."
        },
        {
            "q": "Someone calls claiming to be from the CEO, demanding you wire funds immediately for a confidential acquisition and instructing you not to tell anyone. This is likely:",
            "opts": [
                "A) Business Email Compromise (BEC) / CEO Fraud.",
                "B) A legitimate high-priority business transaction.",
                "C) A standard procedure for quarterly audits."
            ],
            "ans": "A",
            "exp": "Urgency, secrecy, and authority are hallmarks of CEO fraud and Vishing (Voice Phishing). Always verify via out-of-band communication."
        },
        {
            "q": "What is considered the #1 defense against social engineering attacks?",
            "opts": [
                "A) Advanced Firewall protection",
                "B) Security Awareness Training",
                "C) Multi-Factor Authentication (MFA) alone"
            ],
            "ans": "B",
            "exp": "While technical controls help, human behavior is often the final barrier; training equips employees to recognize psychological manipulation."
        }
    ]

    score = 0
    total_questions = len(questions)

    print("=" * 60)
    print("   🛡️  SOCIAL ENGINEERING AWARENESS TRAINING MODULE  🛡️")
    print("=" * 60)
    print_slow(f"Welcome! Let's test your knowledge with {total_questions} scenario-based questions.\n")

    for index, item in enumerate(questions, 1):
        print(f"\n[Question {index} of {total_questions}]")
        print_slow(item["q"])
        print("-" * 60)
        for opt in item["opts"]:
            print(opt)
        print("-" * 60)

        # Input validation loop
        while True:
            user_answer = input("Your answer (A, B, or C): ").strip().upper()
            if user_answer in ["A", "B", "C"]:
                break
            print("❌ Invalid input. Please enter A, B, or C.")

        # Check answer & provide immediate feedback
        if user_answer == item["ans"]:
            print("\n✅ Correct!")
            score += 1
        else:
            print(f"\n❌ Incorrect. The correct answer was {item['ans']}.")

        print(f"💡 Insight: {item['exp']}")
        print("~" * 60)

    # Final Score Summary
    print("\n" + "=" * 60)
    print("                  TRAINING COMPLETE!                  ")
    print("=" * 60)
    print(f"Your Final Score: {score}/{total_questions} ({(score/total_questions)*100:.0f}%)")
    
    if score == total_questions:
        print("🌟 Excellent work! You have strong security awareness instincts.")
    elif score >= total_questions / 2:
        print("👍 Good job, but review the explanations above to tighten your security posture.")
    else:
        print("⚠️ Consider retaking the module. Phishing simulation programs and repetition will help reduce your risk.")
    print("=" * 60)

if __name__ == "__main__":
    run_quiz()