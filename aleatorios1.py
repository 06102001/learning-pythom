import os
from random import randint, uniform

#randint => Genera numeros aleatorios enteros en un rango especificado por el usuario.
#uniform => Genera numeros aleatorios flotantes o decimales en un rango especificado por el desarrollador.

os.system('clear')

n1 = randint(-100,100)
n2 = uniform(1,50)

print(n1)
print(n2)