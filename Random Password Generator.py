import random
import string

while True:
    print("\n===== RANDOM PASSWORD GENERATOR =====")

    # Get password length
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8 characters!")
            continue

    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # Character type selection
    print("\nChoose character types:")
    print("1. Uppercase letters (A-Z)")
    print("2. Lowercase letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Symbols (!@#$%^&*)")

    choices = input("Enter choices separated by spaces (e.g., 1 2 3): ")

    selected = choices.split()

    # Validate choices
    if (
        len(selected) < 2
        or len(set(selected)) != len(selected)
        or not all(choice in ["1", "2", "3", "4"] for choice in selected)
    ):
        print("Please select at least 2 different valid character types!")
        continue

    # Build character pool
    characters = ""

    if "1" in selected:
        characters += string.ascii_uppercase

    if "2" in selected:
        characters += string.ascii_lowercase

    if "3" in selected:
        characters += string.digits

    if "4" in selected:
        characters += string.punctuation

    # Generate password with at least one character per selected type
    password = []

    if "1" in selected:
        password.append(random.choice(string.ascii_uppercase))

    if "2" in selected:
        password.append(random.choice(string.ascii_lowercase))

    if "3" in selected:
        password.append(random.choice(string.digits))

    if "4" in selected:
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print("\nGenerated Password:", password)

    # Ask whether to generate another password
    again = input("\nGenerate another password? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using the Password Generator!")
        break
