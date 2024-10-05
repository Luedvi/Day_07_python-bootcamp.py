# Step 3
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
game_over = False
while not game_over:  # alternatively "while game_over == False"
    guess = input("Guess a letter: ").lower()

# Check guessed letter
    for index in range(word_length):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter
    print(display)

# Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        print("You win")
        game_over = True
