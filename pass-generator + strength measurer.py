import random
import string
import re

def generate_password(length=8, parts=2):
    #Generate a password by joining multiple random segments.
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    while len(password) < length * parts:
        password += ''.join(random.choice(characters) for _ in range(length))

    return password

def check_strength(password):
    """Evaluate password strength using regex."""
    length_ok = len(password) >= 16
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])

    
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, score
password = generate_password()
strength, score = check_strength(password)

print(f"Generated Password: {password}")
print(f"Strength: {strength} ({score}/5)")
