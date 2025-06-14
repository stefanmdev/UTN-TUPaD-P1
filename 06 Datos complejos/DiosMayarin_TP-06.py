# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
# 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Verificar el diccionario actualizado
print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800 

# Diccionario actualizado (tras añadir las frutas en el punto 1)
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

# Actualizar precios
precios_frutas['Banana'] = 1330    # Actualiza Banana de 1200 → 1330
precios_frutas['Manzana'] = 1700   # Actualiza Manzana de 1500 → 1700
precios_frutas['Melón'] = 2800     # Actualiza Melón de 3000 → 2800

# Verificar cambios
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios.

# Asumiendo que precios_frutas es el diccionario actualizado del punto anterior
precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

# Crear lista solo con los nombres de las frutas (claves del diccionario)
frutas = list(precios_frutas.keys())

# Mostrar la lista resultante
print(frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

# Inicializar el diccionario de contactos
contactos = {}

# Cargar 5 contactos
print("Por favor, ingresa 5 contactos:")
for i in range(5):
    nombre = input(f"Ingresa el nombre del contacto {i+1}: ")
    numero = input(f"Ingresa el número de teléfono de {nombre}: ")
    contactos[nombre] = numero

# Consultar un contacto
nombre_consulta = input("\nIngresa el nombre del contacto a consultar: ")

# Verificar si el contacto existe y mostrar el número
if nombre_consulta in contactos:
    print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print(f"El contacto {nombre_consulta} no existe en la lista.")

# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra. 

# Solicitar la frase al usuario
frase = input("Ingresa una frase: ")

# Dividir la frase en palabras
palabras = frase.split()

# Obtener palabras únicas usando un set
palabras_unicas = set(palabras)

# Contar la frecuencia de cada palabra
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabras] += 1
    else:
        recuento[palabra] = 1

# Mostrar los resultados
print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. 

# Crear un diccionario vacío para almacenar los alumnos y sus notas
alumnos = {}

# Pedir al usuario que ingrese 3 alumnos con sus notas
for i in range(3):
    nombre = input(f"Ingresa el nombre del alumno {i+1}: ")
    nota1 = float(input("Ingresa la primera nota: "))
    nota2 = float(input("Ingresa la segunda nota: "))
    nota3 = float(input("Ingresa la tercera nota: "))
    alumnos[nombre] = (nota1, nota2, nota3)  # Guardar las notas como una tupla

# Calcular y mostrar el promedio de cada alumno
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")  # Mostrar con 2 decimales

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Sets de estudiantes que aprobaron cada parcial
aprobados_parcial1 = {"Juan", "Ana", "Luis", "María", "Carlos"}
aprobados_parcial2 = {"Ana", "Carlos", "Sofía", "Pedro", "Luis"}

# 1. Estudiantes que aprobaron ambos parciales (intersección)
ambos_parciales = aprobados_parcial1 & aprobados_parcial2
print("Aprobaron ambos parciales:", ambos_parciales)

# 2. Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = aprobados_parcial1 ^ aprobados_parcial2
print("Aprobaron solo uno:", solo_uno)

# 3. Lista total de aprobados en al menos un parcial (unión)
total_aprobados = aprobados_parcial1 | aprobados_parcial2
print("Total de aprobados (al menos uno):", total_aprobados)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe. 

# Diccionario inicial de productos y stock
stock_productos = {
    "Manzanas": 50,
    "Bananas": 30,
    "Peras": 40,
    "Naranjas": 60
}

def consultar_stock():
    producto = input("Ingrese el nombre del producto a consultar: ")
    if producto in stock_productos:
        print(f"Stock de {producto}: {stock_productos[producto]} unidades")
    else:
        print(f"El producto {producto} no existe en el inventario")

def agregar_stock():
    producto = input("Ingrese el nombre del producto: ")
    if producto in stock_productos:
        unidades = int(input(f"Ingrese cuántas unidades desea agregar a {producto}: "))
        stock_productos[producto] += unidades
        print(f"Se agregaron {unidades} unidades. Nuevo stock de {producto}: {stock_productos[producto]}")
    else:
        unidades = int(input(f"Ingrese el stock inicial para el nuevo producto {producto}: "))
        stock_productos[producto] = unidades
        print(f"Producto {producto} agregado con {unidades} unidades")

def menu():
    while True:
        print("\n--- GESTIÓN DE STOCK ---")
        print("1. Consultar stock de un producto")
        print("2. Agregar stock a producto existente o nuevo")
        print("3. Ver todos los productos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            consultar_stock()
        elif opcion == "2":
            agregar_stock()
        elif opcion == "3":
            print("\nInventario completo:")
            for producto, cantidad in stock_productos.items():
                print(f"{producto}: {cantidad} unidades")
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú
menu()

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# 
# Agenda inicial con algunos eventos
agenda = {
    ("lunes", "10:00"): "Reunión con el equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("jueves", "09:30"): "Cita médica"
}

def consultar_evento():
    # Pedir día y hora al usuario
    dia = input("Ingrese el día (ej: lunes): ").lower()
    hora = input("Ingrese la hora (ej: 15:00): ")
    
    # Buscar el evento en la agenda
    evento = agenda.get((dia, hora))
    
    if evento:
        print(f"Evento programado: {evento}")
    else:
        print(f"No hay eventos programados para el {dia} a las {hora}")

# Ejemplo de uso
consultar_evento()
 
# # 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 

# Diccionario original (país: capital)
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}

# Invertir el diccionario (capital: país)
invertido = {capital: pais for pais, capital in original.items()}

# Mostrar resultados
print("Diccionario original:", original)
print("Diccionario invertido:", invertido)



