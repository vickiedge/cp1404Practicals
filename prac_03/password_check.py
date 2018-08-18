"""Vicki Edge"""

MIN_LENGTH = 5

def main():
    password = input("Enter password: ")
    if len(password) < MIN_LENGTH:
        print("Invalid password")
        password = input("Enter password: ")
    length = len(password)
    print("*" * (length))

main()