
import sqlite3

#EJERCICIO 1
#defino la funcion convertir a mayusculas
def convertir_a_mayusculas(cadena):
    return cadena.upper()


#comando para conectar a la base de datos
conexion = sqlite3.connect('base_de_datosTP7.db')

#registro de las funciones UDF
conexion.create_function("convertir_a_mayusculas", 1, convertir_a_mayusculas)

#crear un cursor, sirve para realizar las consultas
cursor = conexion.cursor()

cursor.execute('DELETE FROM Personas')

#comando para crear las tabla PERSONA con una columna nombre/NUMEROS con una columna valor
cursor.execute('''CREATE TABLE IF NOT EXISTS Personas (nombre TEXT)''')
#introduccion de datos en la columna nombre
cursor.execute("INSERT INTO Personas (nombre) VALUES ('nicolas')")
cursor.execute("INSERT INTO Personas (nombre) VALUES ('marco')")
cursor.execute("INSERT INTO Personas (nombre) VALUES ('ezequiel')")


#guardado de datos
conexion.commit()

#obtener y mostrar los resultados, en este caso mostrara los nombres en mayuscula 
cursor.execute("SELECT convertir_a_mayusculas(nombre) FROM Personas")

resultados=cursor.fetchall()
for fila in resultados:
    print(fila[0])

import sqlite3

#EJERCICIO 2
# Definir la función calcular_cuadrado
def calcular_cuadrado(numero):
    return numero ** 2

# Conectar a la base de datos
conexion = sqlite3.connect('base_de_datosTP7.db')

# Registrar la función UDF
conexion.create_function("calcular_cuadrado", 1, calcular_cuadrado)

# creacion un cursor
cursor = conexion.cursor()

cursor.execute('DELETE FROM Numeros')

# creacion de la tabla Numeros
cursor.execute('''
CREATE TABLE IF NOT EXISTS Numeros (valor INTEGER)''')

# insertar la informacion de la columna valores
cursor.execute("INSERT INTO Numeros (valor) VALUES (5)")
cursor.execute("INSERT INTO Numeros (valor) VALUES (6)")
cursor.execute("INSERT INTO Numeros (valor) VALUES (9)")

# Guardar los cambios
conexion.commit()

# Realizar la consulta
cursor.execute("SELECT calcular_cuadrado(valor) FROM Numeros")

# Obtener y mostrar los resultados
resultados = cursor.fetchall()
for fila in resultados:
    print(fila[0])

import sqlite3

#Ejercicio 3 T.M.
#Definir funcion agregada que calcule el promedio de una columna

def promedio(values):
    return sum (values)/ len(values) 

#Conectar a la base de datos y registrar la funcion agregada
conexion=sqlite3.connect('base_de_datosTP7.db')

#Registrar la funcion UDF
conexion.create_aggregate('promedio'), 1, promedio

#Creacion de un cursor
cursor=conexion.cursor()
cursor.execute('DELETE FROM Notas')

#Creacion de la tabla Notas
cursor.execute('''CREATE TABLE IF NOT EXISTS Notas (calificaciones REAL)''')

#Rellenar la informacion de las columnbas calificaciones
cursor.execute("INSERT INTO Notas (calificaciones) VALUES (8.5)")
cursor.execute("INSERT INTO Notas (calificaciones) VALUES (7.5)")
cursor.execute("INSERT INTO Notas (calificaciones) VALUES (9.0)")
cursor.execute("INSERT INTO Notas (calificaciones) VALUES (6.5)")
cursor.execute("INSERT INTO Notas (calificaciones) VALUES (5.5)")

#Guardar los cambios
conexion.commit()

#Realizar la consulta
cursor.execute("SELECT promedio(calificacion) FROM Notas")

#Obtener y mostrar resultados
resultado = cursor.fetchone()
promedio_calificaciones = resultado[0]

print(f"El promedio de las calificaciones es: {promedio_calificaciones:.2f}")

import sqlite3

#Ejercicio 4 T.M.
#Definir la funcion si una palabra es polindromo 
def palindromo(palabra):
    return palabra == palabra[::-1]

#Conectar a la base de datos y registrar la funcion agregada
conexion=sqlite3.connect('base_de_datosTP7.db')

#Registrar la funcion UDF
conexion.create_aggregate('palindromo'), 1, palindromo

#Creacion de un cursor
cursor=conexion.cursor()
cursor.execute('DELETE FROM Palabras')

#Creacion de la tabla palabras
cursor.execute('''CREATE TABLE IF NOT EXISTS Palabras (palabra TEXT)''')

#Insertar palabras
cursor.execute("INSERT INTO Palabras (palabra) VALUES (reconocer)")
cursor.execute("INSERT INTO Palabras (palabra) VALUES (python)")
cursor.execute("INSERT INTO Palabras (palabra) VALUES (oso)")
cursor.execute("INSERT INTO Palabras (palabra) VALUES (casa)")
cursor.execute("INSERT INTO Palabras (palabra) VALUES (radar)")

#guardar los cambios
conexion.commit()

#Realizar la consulta
cursor.execute("SELECT palabra FROM Palabras WHERE palindromo(palabra)")

#Obtener y mostrar resultados
palabras_palindromas = cursor.fetchall()

print("Palabras palíndromas:")
for palabra in palabras_palindromas:
    print(palabra[0])

#Cerrar cesion
conexion.close()
