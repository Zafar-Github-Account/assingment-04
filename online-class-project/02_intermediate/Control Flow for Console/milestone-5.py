import random

NUM_ROUNDS = 3  # You can change this value to control how many rounds the user plays.

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0  # Initialize score to 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        computer_number = random.randint(1, 100)
        user_number = random.randint(1, 100)

        print(f"Your number is {user_number}")
        
        # Safeguard user input
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        
        while guess not in ["higher", "lower"]:
            guess = input("Please enter either 'higher' or 'lower': ").strip().lower()

        if guess == "higher":
            if user_number > computer_number:
                print(f"You were right! The computer's number was {computer_number}")
                score += 1  # Increase score if correct
            else:
                print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        elif guess == "lower":
            if user_number < computer_number:
                print(f"You were right! The computer's number was {computer_number}")
                score += 1  # Increase score if correct
            else:
                print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}")
        print()  # Blank line to separate rounds visually

    # Conditional ending messages based on score
    if score == NUM_ROUNDS:
        print(f"Your score is now {score}")
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print(f"Your score is now {score}")
        print("Good job, you played really well!")
    else:
        print(f"Your score is now {score}")
        print("Better luck next time!")

if __name__ == '__main__':
    main()
