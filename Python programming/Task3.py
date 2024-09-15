import random
import string

def generate_password(length, complexity):
    if complexity == '1':
        characters = string.ascii_lowercase
    elif complexity == '2':
        characters = string.ascii_letters
    elif complexity == '3':
        characters = string.ascii_letters + string.digits
    elif complexity == '4':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Choose between 1 and 4.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("Specify the length of the password:")
    while True:
        try:
            length = int(input("Enter length: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

    print("Specify the complexity level:")
    print("1. Lowercase letters only")
    print("2. Uppercase and lowercase letters")
    print("3. Letters and digits")
    print("4. Letters, digits, and special characters")

    while True:
        try:
            complexity = input("Enter complexity level (1/2/3/4): ")
            if complexity not in ['1', '2', '3', '4']:
                raise ValueError("Invalid choice. Please enter a number between 1 and 4.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    password = generate_password(length, complexity)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
