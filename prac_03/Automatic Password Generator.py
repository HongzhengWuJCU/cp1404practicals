import random
import string

def check_password(password, length, required_groups):
    """Check the length and required character types."""
    if len(password) != length:
        return False
    for group in required_groups:
        if not any(character in group for character in password):
            return False
    return True

def main():
    length = int(input("Password length: "))
    required_groups = []
    if input("Require uppercase letters? (y/n): ").lower() == "y":
        required_groups.append(string.ascii_uppercase)
    if input("Require lowercase letters? (y/n): ").lower() == "y":
        required_groups.append(string.ascii_lowercase)
    if input("Require numbers? (y/n): ").lower() == "y":
        required_groups.append(string.digits)
    if input("Require special characters? (y/n): ").lower() == "y":
        required_groups.append(string.punctuation)
    if not required_groups:
        print("Select at least one character type.")
        return
    if length < len(required_groups):
        print("Length must be at least", len(required_groups))
        return
    # Include one character from every required type.
    characters = []
    for group in required_groups:
        characters.append(random.choice(group))
    # Fill the remaining spaces using the selected types.
    allowed_characters = "".join(required_groups)
    while len(characters) < length:
        characters.append(random.choice(allowed_characters))
    # Mix the characters and convert the list into a string.
    random.SystemRandom().shuffle(characters)
    password = "".join(characters)
    if check_password(password, length, required_groups):
        print("Password:", password)
        print("Password meets all requirements.")
    else:
        print("Password failed validation.")


main()