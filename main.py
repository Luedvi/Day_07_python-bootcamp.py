# Step 4
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

game_over = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for index in range(word_length):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter
    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1. If lives goes down to 0 then the game should stop and it should print "You lose."
    if not guess in display:
        lives -= 1
        if lives == 0:  # this nested "if" can also be at the same indentation level as the "if" above, the result is the same
            game_over = True
            print("You lose")
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        game_over = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    if lives == 6:
       print(stages[6])
    elif lives == 5:
       print(stages[5])
    elif lives == 4:
       print(stages[4])
    elif lives == 3:
       print(stages[3])
    elif lives == 2:
       print(stages[2])
    elif lives == 1:
       print(stages[1])
    else:
       print(stages[0])
