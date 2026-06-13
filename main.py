length=int(input("Enter the passwordlength:"))
if length<4:
    print("Password length should be at least 4 characters.")
else:
    import random
    import string

    # Define the character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password includes at least one character from each set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the remaining length with a mix of all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness and convert to a string
    random.shuffle(password)
    final_password = ''.join(password)

    print("Generated Password:", final_password)