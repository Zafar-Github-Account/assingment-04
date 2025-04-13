import random

def guess_number():
    print("Welcome to the Guess the Number game!")
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))

    number = random.randint(lower, upper)
    guess = None
    attempts = 0

    while guess != number:
        try:
            guess = int(input(f"Guess a number between {lower} and {upper}: "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {number} in {attempts} tries.")
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
guess_number()
