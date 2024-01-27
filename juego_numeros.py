'''
Este código implementa un juego simple donde el usuario intenta adivinar 
un número generado aleatoriamente entre 1 y 100. Utiliza un bucle while
para permitir múltiples intentos y maneja la entrada del usuario con un 
bloque try y except para asegurarse de que se ingrese un número entero 
válido. Además, proporciona mensajes indicando si la suposición es mayor
o menor que el número secreto.
'''

import random

def juego_de_numeros():
    print("¡Bienvenido al juego de números!")
    numero_secreto = random.randint(1, 10)
    intentos = 0
    adivinado = False

    print("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinar!")

    while not adivinado:
        try:
            suposicion = int(input("Tu suposición: "))
            intentos += 1

            if suposicion == numero_secreto:
                adivinado = True
                print(f"¡Correcto! Has adivinado el número en {intentos} intentos.")
            elif suposicion < numero_secreto:
                print("El número es mayor. Intenta nuevamente.")
            else:
                print("El número es menor. Intenta nuevamente.")

        except ValueError:
            print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    juego_de_numeros()
