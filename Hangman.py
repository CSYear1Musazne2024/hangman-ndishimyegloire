ASSIGNMENT 2 SOLUTION:



import random
import string

def load_words(filename):
    """Load words from the file and return them as a list."""
    try:
        with open(filename, 'r') as file:
            return file.read().split()
    except FileNotFoundError:
        print("Error: words.txt file not found.")
        return []

def choose_word(wordlist):
    """Choose a random word from the wordlist."""
    return random.choice(wordlist) if wordlist else None

def is_word_guessed(secret_word, letters_guessed):
    """Check if all letters of the secret word have been guessed."""
    return all(letter in letters_guessed for letter in secret_word)

def get_guessed_word(secret_word, letters_guessed):
    """Return the current guessed state of the word."""
    return ''.join(letter if letter in letters_guessed else '-' for letter in secret_word)

def get_available_letters(letters_guessed):
    """Return the letters that have not been guessed yet."""
    return ''.join(letter for letter in string.ascii_lowercase if letter not in letters_guessed)

def hangman():
    # Sample word list embedded directly into the program
    sample_words = "apple banana orange grape cherry"
    wordlist = sample_words.split()

    secret_word = choose_word(wordlist).lower()
    if not secret_word:
        print("No word available for the game.")
        return

    guesses_remaining = 10
    warnings_remaining = 3
    letters_guessed = []

    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("-------------")

    while guesses_remaining > 0:
        if is_word_guessed(secret_word, letters_guessed):
            print(f"Congratulations, you won! The word was '{secret_word}'.")
            return

        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        guess = input("Please guess a letter: ").lower()

        if not guess.isalpha():  # Non-alphabet input
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left.")
            else:
                guesses_remaining -= 1
                print(f"Oops! That is not a valid letter. You have no warnings left, so you lose one guess.")
            print("-------------")
            continue

        if guess in letters_guessed:  # Already guessed
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left.")
            else:
                guesses_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have no warnings left, so you lose one guess.")
            print("-------------")
            continue

        letters_guessed.append(guess)

        if guess in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        else:
            if guess in 'aeiou':  # Vowels cost 2 guesses
                guesses_remaining -= 2
            else:  # Consonants cost 1 guess
                guesses_remaining -= 1
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")

        print("-------------")

    print(f"Sorry, you ran out of guesses. The word was '{secret_word}'.")

# Run the game
hangman()
