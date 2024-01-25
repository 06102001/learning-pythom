'''
Calculadora que reciba 2 numeros y
realice la operacion aritmetica que el usuario desee.
puede escoger entre sumar, restar, multiplicar o dividir

'''
import os
os.system ("clear")

def calculator(x, y, z):
    if z == '1' :
        return x + y
    elif z == '2' :
        return x - y
    elif z == '3' :
        return  x * y
    elif z == '4' :
        if y == 0:
            return 'No es posible dividir entre cero'
        else:
            return x / y
    elif z == '5' :
        if y == 0:
            return x + y, x - y, x * y, 'No es posible dividir entre cero (0)'
        else:
            return x + y, x - y, x * y, x / y
    else :
        return 'Fail, invalid option'

n1 = float(input("Ingrese primer valor: "))
n2 = float(input("Ingrese segundo valor: "))

print(":::MENU CALCULADORA:::")
print("[1]. Sumar")
print("[2]. Restar")
print("[3]. Multiplicar")
print("[4]. Dividir")
print("[5]. Todas")
opc = input ("Digite una opcion del menu: ")

#Formato de salida 1
ans = calculator(n1, n2, opc)
print("Resultado :", ans)
#Formato de salida 2
print("resultado", calculator(n1, n2, opc))
#Formato de salida 3
if opc == '1' or opc == '2' or opc == '3' or opc == '4':
    ans = calculator(n1, n2, opc)
    print("Resultado: ", ans)
elif opc == '5':
    ans = calculator(n1, n2, opc)
    print("Suma:", ans[0])
    print("Resta:", ans[1])
    print("Multiplicación:", ans[2])
    print("Divisón:", ans[3])