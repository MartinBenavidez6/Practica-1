import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_attempts = 5
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
dificultad = int(input("Elegir dificultad por nivel del 1 al 3: "))
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
if dificultad == 1:
    word_displayed = ''.join([letter if letter in 'aeiouáéíóú' else '_' for letter in secret_word])
    guessed_letters.extend("aeiouáéíóú")
elif dificultad == 2:
    word_displayed = secret_word[0] + '_' * (len(secret_word) - 2) + secret_word[-1]
    guessed_letters.extend(secret_word[0] + secret_word[-1])
else:
    word_displayed = '_' * len(secret_word)  
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
attempts = 0
while attempts != max_attempts:
     # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word and letter != "":
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        attempts = attempts + 1
    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
 # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")
