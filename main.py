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

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

spanish_word_list = [
    "paraninfo",
    "inusual",
    "arqueozoología",
    "indiscernible",
    "abasto",
    "repentino",
    "recolecta",
    "arboricidio",
    "recompensable",
    "asegurado",
    "rehabilitación",
    "clavadista",
    "superlativo",
    "casto",
    "tiránico",
    "apalancar",
    "raudo",
    "primacía",
    "previsorio",
    "requilorio",
    "detraimiento"]

clues = [
    "En algunas universidades, salón de actos",
    "No usual, infrecuente.",
    "Parte de la arqueología que se ocupa especialmente del estudio de restos de animales en yacimientos de antiguas culturas.",
    "Que no se puede discernir.",
    " Provisión de bastimentos, y especialmente de víveres.",
    "Pronto, impensado, no previsto",
    "Acción de recolectar.",
    "Tala injustificada de árboles",
    "Digno de recompensa.",
    "Protegido de las consecuencias de un riesgo mediante un seguro",
    "Conjunto de métodos que tiene por finalidad la recuperación de una actividad o función perdida o disminuida por traumatismo o enfermedad.",
    "Deportista que efectúa clavados o saltos de trampolín",
    "Muy grande o desmesurado",
    "Dicho de una persona: Que se abstiene de todo goce sexual, o se atiene a lo que se considera como lícito.",
    "Perteneciente o relativo a la tiranía",
    "Levantar, mover algo con ayuda de una palanca.",
    "Rápido, violento, precipitado",
    "Cajón corredizo que hay en los escritorios y sirve para guardar lo que se quiere tener a mano.",
    "Superioridad, ventaja o excelencia que algo tiene con respecto a otra cosa de su especie.",
    "Que incluye previsión, prudencia y sensatez.",
    "Adorno o complemento excesivo o innecesario",
    "Infamia, deshonor"]

from random import choice
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


try_again = True

while try_again:
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
                    print("Â¡Felicidades! adivinaste la palabra secreta")

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

    if input("¿quieres seguir jugando? Escribe 's' para si, 'n' para terminar el juego: ") != "s":
        try_again = False
    else:
        clear()
