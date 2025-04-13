import random

choices = ['rock', 'paper', 'scissors']

def get_user_choice():
    while True:
        print("\nChoose:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        try:
            selection = int(input("Enter the number of your choice (1-3): "))
            if 1 <= selection <= 3:
                return choices[selection - 1]
            else:
                print("❌ Invalid number. Please enter 1, 2, or 3.")
        except ValueError:
            print("❌ Please enter a valid number (1, 2, or 3).")

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return 'user'
    else:
        return 'computer'

def play_round():
    user = get_user_choice()
    computer = get_computer_choice()

    print(f"\n🧍 You chose: {user}")
    print(f"🤖 Computer chose: {computer}")

    winner = determine_winner(user, computer)

    if winner == 'tie':
        print("⚖️ It's a tie!")
    elif winner == 'user':
        print("🎉 You win this round!")
    else:
        print("💻 Computer wins this round!")

    return winner

def play_game():
    print("\n🔥 Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0
    round_number = 1

    while user_score < 3 and computer_score < 3:
        print(f"\n🔁 Round {round_number}")
        winner = play_round()

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"Score → You: {user_score} | Computer: {computer_score}")
        round_number += 1

    if user_score == 3:
        print("\n🏆 Congratulations! You won the game!")
    else:
        print("\n👾 The computer won the game. Better luck next time!")

def start():
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != 'yes':
            print("👋 Thanks for playing! Bye!")
            break

# Run the game
start()
