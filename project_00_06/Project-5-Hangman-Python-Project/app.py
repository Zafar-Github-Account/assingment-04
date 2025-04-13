import random
import string

# Word list by categories
categories = {
    'animals': ['dog', 'cat', 'elephant', 'giraffe', 'kangaroo'],
    'movies': ['inception', 'matrix', 'titanic', 'avatar', 'joker'],
    'countries': ['canada', 'brazil', 'germany', 'japan', 'australia']
}

# Hangman ASCII art for each wrong guess
hangman_art = [
    '''
     ------
     |    |
          |
          |
          |
          |
    ''', 
    '''
     ------
     |    |
     O    |
          |
          |
          |
    ''',
    '''
     ------
     |    |
     O    |
     |    |
          |
          |
    ''',
    '''
     ------
     |    |
     O    |
    /|    |
          |
          |
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    '''
]

# Function to select a word from a category
def get_valid_word(category):
    word = random.choice(categories[category])
    while '-' in word or ' ' in word:
        word = random.choice(categories[category])
    return word.upper()

# Function to display the current hangman state
def display_hangman(lives):
    print(hangman_art[6 - lives])

# Function to handle the game logic
def hangman():
    print("🎮 Welcome to Advanced Hangman!")
    
    # Select difficulty level
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    if difficulty == 'easy':
        word_list = [word for category in categories.values() for word in category if len(word) <= 4]
    elif difficulty == 'medium':
        word_list = [word for category in categories.values() for word in category if 5 <= len(word) <= 7]
    else:
        word_list = [word for category in categories.values() for word in category if len(word) > 7]

    # Select category
    category = input("Choose category (animals, movies, countries): ").lower()
    while category not in categories:
        print("❌ Invalid category. Choose from animals, movies, or countries.")
        category = input("Choose category (animals, movies, countries): ").lower()

    word = get_valid_word(category)
    word_letters = set(word)  # letters to guess
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters guessed
    lives = 6
    score = 0

    while len(word_letters) > 0 and lives > 0:
        display_hangman(lives)
        
        # Show current word status
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("Word: ", ' '.join(word_display))

        print(f"You've used: {' '.join(used_letters)}")
        print(f"Lives left: {lives}")
        
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("✅ Correct!")
            else:
                lives -= 1
                print("❌ Wrong guess!")
        elif user_letter in used_letters:
            print("⚠️ You've already guessed that letter.")
        else:
            print("❌ Invalid character. Please enter a letter.")

    if lives == 0:
        display_hangman(lives)
        print(f"\n💀 You died! The word was: {word}")
    else:
        score += 1
        print(f"\n🎉 You guessed the word: {word}")
        print(f"Your score: {score}")
    
    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman()
    else:
        print("👋 Thanks for playing! Goodbye!")

# Run the game
hangman()
