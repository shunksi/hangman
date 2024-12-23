import random

# Function to display the hangman stages
def display_hangman(attempts):
    stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    return stages[6 - attempts]

# Main Hangman game function
def hangman():
    # List of words for the game
    words = ['python', 'programming', 'hangman', 'developer', 'hope', 'hangman', 'repository']
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print(display_hangman(attempts))
    print(" ".join(guessed_word))

    while attempts > 0 and '_' in guessed_word:
        guess = input("\nGuess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter a single letter.")
            continue

        # Check if letter is already guessed
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        # Update game state
        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_word[idx] = guess
            print("\nGood guess!")
        else:
            attempts -= 1
            print(f"\nWrong guess! Attempts left: {attempts}")
        
        # Display updated hangman and word
        print(display_hangman(attempts))
        print(" ".join(guessed_word))

    # End of the game
    if '_' not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
