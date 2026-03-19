import re

password = input("Enter your password: ")

# Conditions
length = len(password) >= 8
has_upper = re.search(r"[A-Z]", password)
has_number = re.search(r"[0-9]", password)
has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

# Check strength
if length and has_upper and has_number and has_special:
    print("✅ Strong Password")
else:
    print("❌ Weak Password")