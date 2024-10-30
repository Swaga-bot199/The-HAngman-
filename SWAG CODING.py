import random

def hangman():
    # List of words for the game
    words = ["python", "hangman", "computer", "programming", "algorithm"]
    word = random.choice(words)  # Randomly select a word
    guessed_letters = []  # List to keep track of guessed letters
    attempts = 6  # Number of attempts

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        # Display the current state of the word
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        # Ask the player for a guess
        guess = input("Guess a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guess is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")
            print(f"You have {attempts} attempts remaining.")

        # Check if the player has guessed all the letters
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break

    # If player runs out of attempts
    if attempts == 0:
        print(f"Game over! The word was: {word}")

# Run the game
hangman()
