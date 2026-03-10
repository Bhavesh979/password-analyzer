import re
import random
import string


def check_password_strength(password):

    score = 0
    feedback = []

    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_number = bool(re.search(r"[0-9]", password))
    has_special = bool(re.search(r"[!@#$%^&*]", password))

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters.")

    if has_upper:
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if has_lower:
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if has_number:
        score += 1
    else:
        feedback.append("Add numbers.")

    if has_special:
        score += 1
    else:
        feedback.append("Add special characters.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {
        "strength": strength,
        "score": score,
        "length": len(password),
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_number": has_number,
        "has_special": has_special,
        "feedback": feedback
    }


def generate_strong_password():

    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    password = ''.join(random.choice(chars) for _ in range(12))

    return password
