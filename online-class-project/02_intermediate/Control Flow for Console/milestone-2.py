import random

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    computer_number = random.randint(1, 100)
    user_number = random.randint(1, 100)

    print(f"The computer's number is {computer_number}")
    print(f"Your number is {user_number}")

    guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

    # Just for now, print the guess to confirm
    print(f"You guessed: {guess}")

if __name__ == '__main__':
    main()

