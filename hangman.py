import random

MAX_ATTEMPTS = 6

HANGMAN_PICTURES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

WORDS = [
    "python",
    "computer",
    "keyboard",
    "programming",
    "function",
    "variable",
    "developer",
    "algorithm",
    "internet",
    "hangman",
    "software",
    "student",
    "terminal",
    "practice",
    "science"
]


def show_word(secret_word, guessed_letters):
    """Show known letters and underscores for letters not guessed yet."""
    displayed_letters = []

    for letter in secret_word:
        if letter in guessed_letters:
            displayed_letters.append(letter.upper())
        else:
            displayed_letters.append("_")

    return " ".join(displayed_letters)


def get_letter(guessed_letters):
    """Ask the player for one new English letter."""
    while True:
        letter = input("Guess a letter (A-Z): ").strip().lower()

        if len(letter) != 1 or letter not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter one English letter from A to Z.")
        elif letter in guessed_letters:
            print("You have already guessed that letter. Try another one.")
        else:
            return letter


def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_letters = set()

    print("\nWelcome to Hangman!")
    print("Guess the hidden word one letter at a time.")
    print(f"You can make {MAX_ATTEMPTS} wrong guesses.")

    while len(wrong_letters) < MAX_ATTEMPTS:
        mistakes = len(wrong_letters)
        print(HANGMAN_PICTURES[mistakes])
        print("\nWord: " + show_word(secret_word, guessed_letters))

        if wrong_letters:
            print("Wrong letters: " + ", ".join(sorted(wrong_letters)).upper())
        else:
            print("Wrong letters: none")

        if all(letter in guessed_letters for letter in secret_word):
            break

        guess = get_letter(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct! That letter is in the word.")
        else:
            wrong_letters.add(guess)
            print("Sorry, that letter is not in the word.")

        if all(letter in guessed_letters for letter in secret_word):
            break

    print(HANGMAN_PICTURES[len(wrong_letters)])
    print("\nWord: " + show_word(secret_word, guessed_letters))

    if all(letter in guessed_letters for letter in secret_word):
        print("\nYou win! Well done.")
    else:
        print("\nGame over. You used all six wrong guesses.")
        print("The hidden word was: " + secret_word.upper())


if __name__ == "__main__":
    try:
        play_hangman()
    except (KeyboardInterrupt, EOFError):
        print("\nGame ended. Thanks for playing!")
