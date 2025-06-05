print("Programa que utilizaré de ejemplo para crear codigo en Python")
# Python se le linea por linea así para hacer más legible el codigo y a demás para debuggear más facil

# Ejemplo de variables, no se puede declarar las variables con una palabra reservada
nombre = "El pepe" #Esto es una variable tipo STRING
edad = 25 #Esto es una variable tipo INT
altura = 1.75 #Esto es una variable tipo FLOAT o DOUBLE
chambea = True #Esto es una variable tipo BOOLEAN

if edad >= 18:
    print(nombre + "es mayor de edad")
else:
    print(nombre + "es menor de edad")

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