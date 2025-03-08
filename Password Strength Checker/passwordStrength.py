import string
password = input("Enter a password: ")
def evaluate_password(password):
    score = 0
    messages = []
    if len(password) >= 8:
        score += 2
    else:
        messages.append("Your password needs to be at least 8 characters long.")

    if any(c.isupper() for c in password):
        score += 2
    else:
        messages.append("Your password needs at least one uppercase letter.")

    if any(c.islower() for c in password):
        score += 2
    else:
        messages.append("Your password needs at least one lowercase letter.")

    if any(c.isdigit() for c in password):
        score += 2
    else:
        messages.append("Your password needs at least one digit.")

    special_characters = set(string.punctuation)
    if any(c in special_characters for c in password):
        score += 2
    else:
        messages.append("Your password needs at least one special character.")
    if score == 10:
        messages.append("Your password is strong! 💪")
    else:
        messages.append(f"Password Strength: {score}/10")

    return messages, score

messages, score = evaluate_password(password)
for message in messages:
    print(message)

