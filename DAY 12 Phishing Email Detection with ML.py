from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

def train_and_run_detector():
    # 1. Training Dataset (Sample emails and their corresponding labels)
    emails = [
        "Verify your account now or it will be suspended",
        "Click here to claim your prize immediately",
        "Team standup at 3pm, agenda attached",
        "Update your billing details to avoid service interruption",
        "Your package has been delivered, tracking info inside",
        "URGENT: Password reset required due to security breach",
        "Project roadmap review meeting tomorrow morning",
        "Win a free iPhone by clicking this secure link",
        "Hi, please find the quarterly financial report attached.",
        "Your bank account is locked! Click this link to unlock immediately."
    ]

    labels = [
        "phishing", 
        "phishing", 
        "safe", 
        "phishing", 
        "safe", 
        "phishing", 
        "safe", 
        "phishing",
        "safe",
        "phishing"
    ]

    # 2. Create Model Pipeline (Text Vectorization + Naive Bayes Classifier)
    model = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('classifier', MultinomialNB())
    ])

    # 3. Train the model using the dataset
    model.fit(emails, labels)

    print("=" * 60)
    print("   🛡️  PHISHING EMAIL DETECTION SYSTEM (ML)  🛡️")
    print("=" * 60)
    print("Model is trained and ready! You can now test any email.")
    print("Type 'q' to exit the program.\n")

    # 4. Interactive loop to test user-entered emails
    while True:
        user_email = input("✉️ Enter the email text to check:\n> ").strip()
        
        # Exit condition
        if user_email.lower() == 'q':
            print("Exiting program. Goodbye!")
            break
            
        if not user_email:
            print("⚠️ Please enter some text to analyze.\n")
            continue

        # Predict whether the input email is phishing or safe
        prediction = model.predict([user_email])[0]

        # Display the result
        print("-" * 60)
        if prediction == "phishing":
            print("🚨 ALERT: This email is likely 'Phishing' (Fraudulent/Suspicious)!")
        else:
            print("✅ SAFE: This email appears to be legitimate.")
        print("-" * 60 + "\n")

if __name__ == "__main__":
    train_and_run_detector()