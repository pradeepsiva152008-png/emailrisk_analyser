import re

email = input("Paste the email content: ").lower()

risk_words = [
    "urgent", "immediately", "verify your account",
    "password", "bank details", "click here",
    "account suspended", "prize", "won"
]

suspicious_links = re.findall(r"https?://\\S+|www\\.\\S+", email)

found_words = [word for word in risk_words if word in email]

score = len(found_words) + len(suspicious_links)

print("\nEmail Risk Analysis")
if score >= 3:
    print("Risk Level: HIGH")
elif score >= 1:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: LOW")

if found_words:
    print("Suspicious phrases:", ", ".join(found_words))
if suspicious_links:
    print("Links found:", ", ".join(suspicious_links))
if score == 0:
    print("No common suspicious patterns were detected.")

print("\nNote: This is a basic checker. It cannot prove that an email is safe.")
