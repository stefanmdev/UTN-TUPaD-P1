# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(0, 101):
    print(numero)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

numero = int(input("Ingrese un número entero: "))

# Usamos valor absoluto para ignorar el signo negativo
numero = abs(numero)
digitos = 0

if numero == 0:
    digitos = 1
else:
    while numero > 0:
        numero = numero // 10  
        digitos += 1           

print("La cantidad de dígitos es:", digitos)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 

inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

menor = min(inicio, fin)
mayor = max(inicio, fin)

suma = 0

for numero in range(menor + 1, mayor):
    suma += numero

print("La suma de los números entre", menor, "y", mayor, "es:", suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0.

suma = 0
numero = 1  

while numero != 0:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    
    if numero != 0:
        suma += numero

print("La suma total es:", suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random 

numero_secreto = random.randint(0, 9)

intento = -1  
contador_intentos = 0  


while intento != numero_secreto:
    intento = int(input("Adiviná el número (entre 0 y 9): "))
    contador_intentos += 1

print("¡Correcto! Adivinaste en", contador_intentos, "intento(s).")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 


for numero in range(100, -1, -1):
    if numero % 2 == 0:
        print(numero)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

limite = int(input("Ingrese un número entero positivo: "))

suma = 0

for numero in range(0, limite + 1):
    suma += numero

print("La suma de los números entre 0 y", limite, "es:", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad_numeros = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(1, cantidad_numeros + 1):
    numero = int(input("Ingrese el número " + str(i) + ": "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 

cantidad_numeros = 100

suma = 0

for i in range(1, cantidad_numeros + 1):
    numero = int(input("Ingrese el número " + str(i) + ": "))
    suma += numero

media = suma / cantidad_numeros

print("La media de los", cantidad_numeros, "números ingresados es:", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

numero = int(input("Ingrese un número entero positivo: "))

numero_invertido = 0

while numero > 0:
    ultimo_digito = numero % 10
    numero_invertido = numero_invertido * 10 + ultimo_digito
    numero = numero // 10

print("El número invertido es:", numero_invertido)






