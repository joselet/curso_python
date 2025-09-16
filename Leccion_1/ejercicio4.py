import random

secreto = random.randint(1, 10)
intentos = 0

while True:
    intento = int(input("Adivina (1-10): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Adivinaste en {intentos} intentos!")
        break
    elif intento < secreto:
        print("Más alto")
    else:
        print("Más bajo")
