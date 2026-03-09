import re
import random
import string

def check_password_strength(password):

    score=0
    feedback=[]

    if len(password)>=8:
        score+=1
    else:
        feedback.append("Password must be at least 8 characters.")

    if re.search(r"[A-Z]",password):
        score+=1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"[a-z]",password):
        score+=1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"\d",password):
        score+=1
    else:
        feedback.append("Add a number.")

    if re.search(r"[!@#$%^&*]",password):
        score+=1
    else:
        feedback.append("Add a special character.")

    if score<=2:
        strength="Weak"
    elif score<=4:
        strength="Moderate"
    else:
        strength="Strong"

    return strength,feedback,score


def generate_strong_password():

    chars=string.ascii_letters+string.digits+"!@#$%^&*"

    password="".join(random.choice(chars) for _ in range(12))

    return password
