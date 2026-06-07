import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special_char=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_char:
        characters += string.punctuation
    if not characters:
        print("error")
        return None
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter the length of the password: "))
include_uppercase = input("Do you want uppercase letters? (y/n): ").lower() == 'y'
include_lowercase = input("Do you want lowercase letters? (y/n): ").lower() == 'y'
include_digits = input("Do you want digits? (y/n): ").lower() == 'y'
include_special_chars = input("Do you want special characters? (y/n): ").lower() == 'y'

generated_password = generate_password(
    length=password_length,
    uppercase=include_uppercase,
    lowercase=include_lowercase,
    digits=include_digits,
    special_char=include_special_chars
)

if generated_password:
    print("Generated Password:", generated_password)
