import random

def computer_guess():
    print("Think of a number and I'll try to guess it!")
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    feedback = ''
    attempts = 0

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # only one possible number left
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        attempts += 1

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Please enter H, L, or C.")

    print(f"🎉 Yay! I guessed your number {guess} in {attempts} attempts.")

# Run the game
computer_guess()
