print("Programa que utilizaré de ejemplo para crear codigo en Python")
# Python se le linea por linea así para hacer más legible el codigo y a demás para debuggear más facil

# Ejemplo de variables, no se puede declarar las variables con una palabra reservada
nombre = "El pepe" #Esto es una variable tipo STRING
edad = 25 #Esto es una variable tipo INT
altura = 1.75 #Esto es una variable tipo FLOAT o DOUBLE
chambea = True #Esto es una variable tipo BOOLEAN

print("El nombre es " + nombre + ", su edad es " + str(edad) + " donde su altura es " + str(altura) + " y " + str(chambea))
if edad >= 18:
    print(nombre + " es mayor de edad")
else:
    print(nombre + " es menor de edad")
if chambea:
    print(nombre + " chambea")
else:
    print(nombre + " no chambea")

# Ejemplo de variables arimetricos
a = 10
b = 3

suma = a + b   # 13
resta = a - b    # 7
multiplicacion = a * b    # 30
division = a / b   # 3.333333333
división_entera = a // b   # 3
modulo = a % b   # 1
exponenciacion = a ** b   # 1000

# Ejemplos de operadores logicos
a = 10
b = 3

resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False

# Ejemplo de ciclo For
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)

# Ejemplo de ciclo while
contador = 0

while True:
    print(contador)
    contador += 1

    if contador == 5:
        break

# Ejemplo de continue
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

# Ejemplo de pass
for i in range(5):
    pass

# Ejemplo de metodos de listas
frutas = ["manzana", "banana", "naranja"]

frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]

frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]

fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"

frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]

frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]

# Ejemplos de listas de comprensión
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]

# Creación de tuplas
numeros = (1, 2, 3, 4, 5)

print(numeros[0])
print(numeros[2])
print(numeros[4])
print(numeros[0:4])

# Metodos de diccionarios
# Definimos nuestro diccionario
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])

# Esto funciona por si no queremos modificar el diccionario Main y queremos agrear más datos
persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}
persona.update({"chambea": True})
print(persona)

# Conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}

interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}

diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}

diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}