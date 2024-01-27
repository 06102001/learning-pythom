'''
El código proporcionado genera un número aleatorio entre 0 y 100 
utilizando randint, luego llama a la función do_it con ese número
como argumento y finalmente imprime el valor original y el resultado
de la función do_it.
'''
from random import randint

def play(y):
    return y + 1

def do_it(x):
    return play(x * x)

def random_number():
    data = randint(0, 100)
    return data, do_it(data)

ans = random_number()

print(f"Value: {ans[0]}")
print(f"Do-it: {ans[1]}")