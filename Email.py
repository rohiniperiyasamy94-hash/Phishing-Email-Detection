
phishing_keywords = [
    "verify", "account", "bank", "password",
    "click", "login", "lottery", "winner",
    "urgent", "claim", "free", "gift",
    "suspended", "update", "prize"
]

email = input("Enter Email Content:\n")

email_lower = email.lower()

score = 0

for keyword in phishing_keywords:
    if keyword in email_lower:
        score += 1

print("\nPhishing Score:", score)

if score >= 2:
    print("Result: Phishing Email")
else:
    print("Result: Safe Email")