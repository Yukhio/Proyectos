# En este modulo comienza por ver los errores que pueden suceder con la sintaxis
#Try
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")


#Except
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")


#Finally
# try:
#     # Código que puede generar una excepción
#     archivo = open("archivo.txt", "r")
#     # Realizar operaciones con el archivo
# except FileNotFoundError:
#     print("Error: Archivo no encontrado")
# finally:
#     archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción


# # Excepciones persnalizadas
# def funcion():
#     # Código que puede generar una excepción personalizada
#     if condicion:
#         raise Exception("Descripción del error")
# try:
#     funcion()
# except Exception as e:
#     print(f"Error: {str(e)}")


# Entradas/Salidas
# En las entradas supongamos que es como un formulario donde el usuario llena datos
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print(nombre+" eres mayor de edad.")
else:
    print(nombre+" eres menor de edad.")


print("Hola, " + nombre + "!")
print("Tienes " + str(edad) + " años.")


# Escritura de archivos
archivo = open("archivo_creado_python.txt", "w")
archivo.write("Nuevo archivo creado llamado" + archivo.name)
archivo.close()

# Lectura de archivos
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()
