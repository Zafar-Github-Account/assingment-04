import random

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    computer_number = random.randint(1, 100)
    user_number = random.randint(1, 100)

    print(f"The computer's number is {computer_number}")
    print(f"Your number is {user_number}")

if __name__ == '__main__':
    main()
