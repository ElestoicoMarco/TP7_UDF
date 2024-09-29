
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

  

#cierre de la conexion
conexion.close()
