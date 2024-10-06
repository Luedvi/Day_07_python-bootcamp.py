# Step 5
from replit import clear
import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["aardvark", "baboon", "camel"]
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
game_over = False
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages
print(logo)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not game_over:
    guess = input("Guess a letter: ").lower()
    # Use the clear() function imported from replit to clear the screen output between guesses.
    clear()
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print("You've already guessed", guess)
    # Check guessed letter
    for index in range(word_length):
        letter = chosen_word[index]
        # print(f"Current position: {index}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[index] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        game_over = True
        print("You win.")

    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
