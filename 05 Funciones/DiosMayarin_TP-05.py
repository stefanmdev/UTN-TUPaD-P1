# 1. Crear una función llamada imprimir_hola_mundo que imprima por
#  pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#  programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#  2. Crear una función llamada saludar_usuario(nombre) que reciba
#  como parámetro un nombre y devuelva un saludo personalizado.
#  Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
#  principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Por favor, ingresa tu nombre: ")
mensaje_saludo = saludar_usuario(nombre_usuario)
print(mensaje_saludo)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
#  edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#  [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def ingresar_edad():
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if edad > 0:
                return edad
            else:
                print("¡La edad debe ser un número positivo!")
        except ValueError:
            print("¡Error! Debes ingresar un número válido.")

print("\n=== Ingresa tus datos ===")
nombre = input("Nombre: ").strip().capitalize()
apellido = input("Apellido: ").strip().capitalize()
edad = ingresar_edad()
residencia = input("Ciudad de residencia: ").strip().capitalize()

informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.

import math 

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def ingresar_radio():
    while True:
        try:
            radio = float(input("Ingresa el radio del círculo (en metros): "))
            if radio > 0:
                return radio
            print("¡El radio debe ser positivo!")
        except ValueError:
            print("¡Error! Ingresa un número válido.")

print("\n=== Calculadora de Círculo ===")
radio = ingresar_radio()

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"\nÁrea: {area:.2f} m²")          
print(f"Perímetro: {perimetro:.2f} m")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
#  una cantidad de segundos como parámetro y devuelva la cantidad
#  de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600.0

def main():
    entrada = input("Ingrese la cantidad de segundos: ").strip()
    try:
        segundos = float(entrada)
        if segundos < 0:
            print("La cantidad de segundos no puede ser negativa. Terminando el programa.")
            return
    except ValueError:
        print("Por favor ingrese un número válido para los segundos. Terminando el programa.")
        return

    horas = segundos_a_horas(segundos)
    print(f"{segundos:.0f} segundos equivalen a {horas:.2f} horas.")


if __name__ == "__main__":
    main()

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

def tabla_multiplicar(numero):
    print(f"\n--- Tabla del {int(numero)} ---")  
    for i in range(1, 11):
        resultado = numero * i
        print(f"{int(numero)} x {i} = {int(resultado)}")

def ingresar_numero():
    while True:
        try:
            numero = int(input("Ingresa un número entero: ")) 
            return numero
        except ValueError:
            print("¡Error! Ingresa un número entero válido.")

print("\n=== Generador de Tablas de Multiplicar ===")
numero = ingresar_numero()
tabla_multiplicar(numero)

#  7. Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

print("=== OPERACIONES BÁSICAS ===")
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    resultados = operaciones_basicas(num1, num2)
    
    print(f"\nResultados:")
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")

except ValueError:
    print("¡Error! Ingresa números válidos.")

#  8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def ingresar_dato(mensaje):
    while True:
        try:
            dato = float(input(mensaje))
            if dato > 0:
                return dato
            print("¡El valor debe ser positivo!")
        except ValueError:
            print("¡Error! Ingresa un número válido.")

print("\n=== CALCULADORA DE IMC ===")
peso = ingresar_dato("Ingresa tu peso en kg: ")
altura = ingresar_dato("Ingresa tu altura en metros: ")

imc = calcular_imc(peso, altura)
print(f"\nTu IMC es: {imc:.2f}")  

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def ingresar_temperatura():
    while True:
        try:
            temp = float(input("Ingresa la temperatura en °C: "))
            return temp
        except ValueError:
            print("¡Error! Ingresa un número válido (ej: 23.5).")

print("\n=== CONVERSOR DE CELSIUS A FAHRENHEIT ===")
celsius = ingresar_temperatura()
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"\n{celsius}°C equivalen a {fahrenheit:.1f}°F")  

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

def ingresar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("¡Error! Ingresa un número válido (ej: 5 o 7.2).")

print("\n=== CALCULADORA DE PROMEDIO ===")
num1 = ingresar_numero("Ingresa el primer número: ")
num2 = ingresar_numero("Ingresa el segundo número: ")
num3 = ingresar_numero("Ingresa el tercer número: ")

promedio = calcular_promedio(num1, num2, num3)
print(f"\nEl promedio es: {promedio:.2f}")  








