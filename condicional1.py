#Los condicionales
'''
Pueden ser simples o compuestos / anidados
Es necesario usar la tabla de operadores logicos:
> => Mayor o igual que
< => Menor o igual que
= => Asignacion
== => Igual a (Operador de comparacion)
Se usan los valores de expresiones booleanas
'''
n1 = 2
if n1 > 0 : #true or false
    print("El numero ", n1, " es positivo")
elif n1 < 0 :
    print("El numero ", n1, " es negativo")
else:
    print("El valor es cero")