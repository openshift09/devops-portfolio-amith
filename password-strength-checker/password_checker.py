import re

def check_strength(password):
    length = len(password) >= 8
    upper  = re.search(r"[A-Z]", password) is not None
    lower  = re.search(r"[a-z]", password) is not None
    digit  = re.search(r"[0-9]", password) is not None
    special = re.search(r"[@$!%*?&#]", password) is not None
    common = password.lower() in ["password", "123456", "admin", "welcome", "qwerty"]

    score = sum([length, upper, lower, digit, special])

    if common:
        return "Very Weak 🔴 (Common password)"

    if score == 5:
        return "Very Strong 🟢"
    elif score == 4:
        return "Strong 🟡"
    elif score == 3:
        return "Medium 🟠"
    else:
        return "Weak 🔴"

# Ask user for input
password = input("Enter a password to check strength: ")
print("\nPassword Strength:", check_strength(password))
