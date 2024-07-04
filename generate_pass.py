import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

try:
    password_length = int(input("Enter the desired length of the password: "))
    if password_length < 1:
        raise ValueError("Password length must be a positive integer.")
except ValueError as ve:
    print(ve)
else:
    password = generate_password(password_length)
    print("Generated Password:", password)