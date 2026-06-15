Password Generator

Description:

This project is a Python based Password Generator that creates strong and secure passwords. The user can specify the desired password length, and the program generates a password containing uppercase letters, lowercase letters, numbers, and special characters.

The application also validates user input and ensures that the password length is at least 4 characters because the uppercase,lowercase,numbers and special character already produces 4 length.

Features:

>User-defined password length,
>Input validation using try-except,
>Includes uppercase letters (A-Z),
>Includes lowercase letters (a-z),
>Includes numbers (0-9),
>Includes special characters,
>Guarantees at least one character from each category,
>Randomly shuffles characters for better security.

Technologies Used:

>Python 3,
>random module,
>string module.

How It Works:

>The user enters the desired password length,
>The program validates the input,
>The program ensures the password contains 
>At least one uppercase letter,
>At least one lowercase letter,
>At least one digit,
>At least one special character.
>Remaining characters are selected randomly.
>The password is shuffled and displayed to the user.
Example

Input:

Enter the password length: 8

Output:

Generated Password: A#7mP2x!

Project Structure

synent-task4-passwordgenerator-anvith

├── main.py

└── README.md

### Logic of Password Generator

1. The program starts by asking the user to enter the desired password length.

```python
length = int(input("Enter the password length: "))
```

2. The entered value is converted into an integer.

3. The program checks whether the password length is at least 4 characters.

```python
if length < 4:
```

This is necessary because the password must contain:

* One uppercase letter
* One lowercase letter
* One digit
* One special character

4. If the length is less than 4, the program displays an error message and stops password generation.

5. If the length is valid, the program imports the `random` and `string` modules.

6. Different character sets are defined:

```python
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation
```

These provide:

* A–Z uppercase letters
* a–z lowercase letters
* 0–9 digits
* Special symbols such as !, @, #, $, etc.

7. To ensure password strength, the program first selects:

* One uppercase letter
* One lowercase letter
* One digit
* One special character

```python
password = [
    random.choice(uppercase_letters),
    random.choice(lowercase_letters),
    random.choice(digits),
    random.choice(special_characters)
]
```

8. All character sets are combined into a single collection.

```python
all_characters = uppercase_letters + lowercase_letters + digits + special_characters
```

9. The remaining characters required to reach the desired password length are randomly selected from this combined character set.

```python
password += random.choices(all_characters, k=length - 4)
```

10. The password characters are shuffled to ensure randomness.

```python
random.shuffle(password)
```

11. The list of characters is joined into a single string.

```python
final_password = ''.join(password)
```

12. The generated password is displayed to the user.

13. Exception handling is implemented using:

```python
except ValueError:
```

If the user enters invalid input such as text instead of a number, the program displays:

```text
Please enter a valid integer for the password length.
```

and prevents the program from crashing.

14. The final result is a strong random password containing uppercase letters, lowercase letters, numbers, and special characters.
>>>>>>> 9a1e353 (added logic to readme file)
