
import random

# List of secret words
words = ["python", "computer", "hacker", "network", "security"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = set()

# Maximum attempts
attempts = 6

# Hangman stages
hangman = [
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
           |
           |
           |
           |
    ---------
    """
]

print("WELCOME TO HANGMAN GAME!")

while attempts > 0:

    # Display current word
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter.upper() + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Attempts left:", attempts)

    # Check winning condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        break

    # Get user input
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    # Check duplicate guess
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

    # Display hangman
    print(hangman[attempts])

else:
    print("\nGame Over! You lost.")
    print("The correct word was:", secret_word.upper())
