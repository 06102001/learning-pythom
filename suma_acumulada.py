'''
En este código, se inicializa una variable ans en 0 
y se utiliza un bucle while para solicitar al usuario 
que ingrese números. La suma de estos números se almacena 
en la variable ans. Si el usuario ingresa 0, el bucle se 
detiene y se imprime la suma final. Además, hay una función 
llamada example que imprime la suma final, y esta función 
se llama al final del código.
'''
def example():
    ans = 0
    operar = True

    while operar:
        try:
            numero = float(input("Ingresa un número: "))
            ans += numero

            if numero == 0:
                operar = False
            else:
                print(ans)

        except ValueError:
            print("Error.")

    print("El resultado final es:", ans)

example()