import re
import random
import string

def check_password_strength(password):

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters.")

    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search("\d", password):
        score += 1
    else:
        feedback.append("Add a number.")

    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add a special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback


def generate_strong_password():

    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(12))

    return password
