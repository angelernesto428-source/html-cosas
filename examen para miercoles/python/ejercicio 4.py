#4️⃣ Adivina el Número Secreto 🕵
#    - Enunciado: Un juego donde tienes que adivinar un número. ¡El programa te da pistas!
#   - Requerimientos: Usar un while y un if-elif-else para las pistas. Terminar con break al acertar.

import random


print("juego de adivinar un numero super divertidop")



numero_secret = random.randint(1,100)

while True:
    respuesta = int(input("adivina un numero entre 1 y 100: "))

    try:
        respuesta2 = int(respuesta)
    except ValueError:
        print("por favor ingrese un numero valido")
        continue

    if respuesta < numero_secret:
        print("demasiado bajo")

    elif respuesta > numero_secret:
        print("demasiado alto")

    else:
        print("GANADOR,vamos a felicitarte")
        break

