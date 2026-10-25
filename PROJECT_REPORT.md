# Project Report: Hangman Word Guessing Game

**Program:** Datheon Python Programming Internship  
**Project:** Hangman Word Guessing Game (Console)  
**Main file:** `hangman.py`  
**Language:** Python 3

## 1. Objective
The objective is to build an interactive terminal game in which a player guesses a hidden word one letter at a time, with a maximum of six incorrect guesses.

## 2. Tools and libraries
- Python 3
- Python standard library: `random`
- Visual Studio Code or PyCharm can be used to edit and run the program.

No third-party Python packages are needed.

## 3. Main features
1. The program chooses a secret word at random.
2. The word is displayed as underscores for letters that have not been guessed.
3. The player enters one English letter per turn.
4. Correct and incorrect guesses are handled separately.
5. Sets store guessed letters and wrong letters, helping the program prevent duplicate penalties.
6. ASCII hangman art changes as mistakes increase.
7. The game ends with a win message when all letters are guessed, or a game-over message after six incorrect guesses.

## 4. Program logic
1. Choose a random word from the word list.
2. Create empty sets for guessed letters and wrong letters.
3. Display the current hangman picture and masked word.
4. Ask for one valid letter, rejecting invalid input and repeated guesses.
5. Reveal the letter if it occurs in the secret word. Otherwise, record a wrong guess.
6. Repeat until the word is solved or six wrong guesses have been made.
7. Display the final result.

## 5. How to run
Open a terminal in the folder containing `hangman.py` and run:

```bash
python hangman.py
```

If that command is not available on Windows, try:

```bash
py hangman.py
```

## 6. Testing
Run the program and manually check each item below before submitting:

- [ ] The program starts correctly.
- [ ] A correct guess reveals matching letters.
- [ ] A wrong guess updates the hangman art and wrong-guess count.
- [ ] Entering the same letter twice does not add another mistake.
- [ ] Entering more than one character or a non-English letter is rejected.
- [ ] Guessing the full word results in a win.
- [ ] Six incorrect guesses result in a loss and reveal the secret word.

**Testing status:** Complete this checklist only after you have personally run and checked the program.

## 7. Submission checklist
- [ ] Upload `hangman.py` to a public GitHub repository named `Datheon_Python_Internship`.
- [ ] Include this report and the `README.md`.
- [ ] Run the game and verify the tests above.
- [ ] Submit the correct public repository URL in the Datheon Student Workspace.
- [ ] Follow the portal's instructions for the LinkedIn demo post and tagging `@Datheon`.

## 8. Learning reflection
Before submitting, add a short reflection in your own words: what part of the program you understood best, what issue you encountered while testing, and how you fixed it.
