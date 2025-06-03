# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva

# Pedir al usuario un número
numero = int(input("Ingrese un número entero mayor o igual a 1: "))

# Calcular y mostrar el factorial de todos los números desde 1 hasta el ingresado
print("\nFactoriales desde 1 hasta", numero, ":")
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

def fibonacci(n):
    if n == 0:  # Caso base 1
        return 0
    elif n == 1:  # Caso base 2
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Llamada recursiva

# Pedir al usuario un número
posicion = int(input("Ingrese una posición (entero ≥ 0): "))

# Validar que el número sea positivo
if posicion < 0:
    print("¡Error! La posición debe ser ≥ 0.")
else:
    # Mostrar la serie completa hasta la posición indicada
    print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
    for i in range(posicion + 1):
        print(f"Fib({i}) = {fibonacci(i)}")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 

def potencia(base, exponente):
    if exponente == 0:  # Caso base: cualquier número elevado a 0 es 1
        return 1
    else:
        return base * potencia(base, exponente - 1)  # Llamada recursiva

# Pedir al usuario la base y el exponente
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero ≥ 0): "))

# Validar que el exponente no sea negativo
if exponente < 0:
    print("¡Error! El exponente debe ser ≥ 0.")
else:
    resultado = potencia(base, exponente)
    print(f"\n{base} elevado a {exponente} es: {resultado}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 

def decimal_a_binario(n):
    if n == 0:  # Caso base 1
        return "0"
    elif n == 1:  # Caso base 2
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)  # Llamada recursiva

# Pedir al usuario un número decimal
numero = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if numero < 0:
    print("¡Error! El número debe ser ≥ 0.")
else:
    binario = decimal_a_binario(numero)
    print(f"\nEl número {numero} en binario es: {binario}")