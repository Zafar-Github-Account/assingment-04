import random

NUM_ROUNDS = 3  # You can change this value to control how many rounds the user plays.

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        computer_number = random.randint(1, 100)
        user_number = random.randint(1, 100)

        print(f"Your number is {user_number}")
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

        if guess == "higher":
            if user_number > computer_number:
                print(f"You were right! The computer's number was {computer_number}")
            else:
                print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        elif guess == "lower":
            if user_number < computer_number:
                print(f"You were right! The computer's number was {computer_number}")
            else:
                print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        else:
            print("Invalid input! Please type 'higher' or 'lower'.")
        
        print()  # Blank line to separate rounds visually

if __name__ == '__main__':
    main()
