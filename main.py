from hangman_art import logo, stages
from random import choice
from hangman_words import spanish_word_list, clues
from replit import clear

chosen_word = choice(spanish_word_list)
clue_index = spanish_word_list.index(chosen_word)
word_length = len(chosen_word)
display = []
game_over = False
lives = len(stages) - 1
for letter in chosen_word:
    display += "_"

print(logo)

while not game_over:
    guess = input("Adivina la palabra secreta. Escribe una letra o escribe 'pista' para ver información de la palabra: ").lower()
    clear()

    if guess in display:
        print("ya adivinaste esta letra")

    for index in range(word_length):
        if chosen_word[index] == guess:
            display[index] = guess
            if "_" not in display:  # can be a nested "if" or not, it doesn't affect the outcome
                game_over = True
                print("¡Felicidades! adivinaste la palabra secreta")

    print(" ".join(display))

    if guess == "pista":
        print("pista: ", clues[clue_index])
    elif guess not in chosen_word:
        lives -= 1
        if lives == 0:  # can be a nested "if" or not, it doesn't affect the outcome
            game_over = True
            print("Se te acabaron las oportunidades. Has perdido el juego")
        else:
            print(f"La letra {guess} no se encuentra en la palabra secreta. Tienes una oportunidad menos")
    print(stages[lives])
