import re
import random
import string
import math

def check_password_strength(password):

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search("\d", password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    entropy = calculate_entropy(password)

    return strength, feedback, entropy


def calculate_entropy(password):

    charset = 0

    if re.search("[a-z]", password):
        charset += 26

    if re.search("[A-Z]", password):
        charset += 26

    if re.search("\d", password):
        charset += 10

    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)

    return round(entropy,2)


def generate_strong_password():

    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    password = ''.join(random.choice(characters) for _ in range(12))

    return password
