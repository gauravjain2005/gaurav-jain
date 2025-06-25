import random
import string

def generate_password(length=12, use_symbols=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Base character sets
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # !@#$%^&*()...

    # Combine characters
    characters = letters + digits
    if use_symbols:
        characters += symbols

    # Ensure at least one of each (for stronger password)
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]
    if use_symbols:
        password.append(random.choice(symbols))

    # Fill the rest of the password
    password += random.choices(characters, k=length - len(password))

    # Shuffle for randomness
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    print("Random Password Generator")
    length = int(input("Enter desired password length (min 4): "))
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
