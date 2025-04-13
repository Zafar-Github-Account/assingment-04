import random

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    computer_number = random.randint(1, 100)
    user_number = random.randint(1, 100)

    print(f"The computer's number is {computer_number}")
    print(f"Your number is {user_number}")

    guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

    if guess == "higher":
        if user_number > computer_number:
            print(f"You were right! The computer's number was {computer_number}")
        else:
            print(f"Sorry, you were wrong. The computer's number was {computer_number}")
    elif guess == "lower":
        if user_number < computer_number:
            print(f"You were right! The computer's number was {computer_number}")
        else:
            print(f"Sorry, you were wrong. The computer's number was {computer_number}")
    else:
        print("Invalid input! Please type 'higher' or 'lower'.")

if __name__ == '__main__':
    main()
