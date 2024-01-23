'''
Script description:
Cree una funcion que genere el lanzamiento de 2 dados (1-6) 
y que muestre por pantalla el mensaje ganador cuando 
genere un par de numeros iguales, de lo contrario dira (sigue intentando)
'''
#Importo bliblioteca para generar numeros aleatorios enteros.
from random import randint

#Lanzar para gnerar los valores de los dos dados.
def dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)

    return dice1, dice2

#Salidas
d = dices()
d1 = d[0]
d2 = d[1]

print("Dices: ", d)
print ("Dice 1:", d1)
print ("Dice 2:", d2)


if d1==d2:
    print("Felicidades eres el Ganador")
    else:
    print("sigue intentando")

#print("Dice1 :", dice1)
#print("Dice2 :", dice2)
