import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length for your password: "))
        if length <= 0:
            print("Please enter a valid length greater than zero.")
            return
        password = generate_password(length)
        print("Your generated password is:", password)
    except ValueError:
        print("Please enter a valid number for the password length.")

main()  # Call the main function directly without using _name_ == "_main_"
