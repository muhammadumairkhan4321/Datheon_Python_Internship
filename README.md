# Datheon Python Internship — Hangman Game

## Project overview
This is a console-based Hangman word guessing game written in Python. The computer chooses a word, and the player tries to reveal it by guessing one letter at a time.

## Features
- Selects a random word using Python's `random` module.
- Gives the player up to six incorrect guesses.
- Shows ASCII hangman art after each incorrect guess.
- Displays letters already guessed and the current word pattern.
- Rejects invalid input and repeated guesses.
- Shows a clear win or game-over message.

## Requirements
- Python 3
- No third-party packages are required.

## How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python hangman.py
   ```

   On some Windows systems, use `py hangman.py`.

## How to play
- Type one English letter from A to Z and press Enter.
- Correct guesses reveal that letter in the word.
- Incorrect guesses add one mistake.
- Repeated guesses do not add a mistake.
- Guess the complete word before six incorrect guesses to win.

## Files
- `hangman.py` — game source code.
- `PROJECT_REPORT.md` — short project report.

## Testing checklist
Before submitting, run the game and check:
- [ ] The game starts without an error.
- [ ] A correct letter is shown in the word.
- [ ] A wrong letter increases the mistake count.
- [ ] A repeated letter does not increase the mistake count.
- [ ] The player wins after revealing all letters.
- [ ] The player loses after six incorrect guesses.

## Notes
The word list is currently defined in `WORDS` inside `hangman.py`. You can add more lowercase English words to that list.
