#EJERCICIOS DE DICCIONARIOS
"""
Nombre: Stalin Gutama
Carrera: Big Data
"""

#Crear un diccionario vacío:

dicc = {}

#Agregar elementos a un diccionario:

dicc["Clave 1"] = 100
dicc["Clave 2"] = 200
dicc["Clave 3"] = 300
dicc["Clave 4"] = 400
dicc["Clave 5"] = 500

print(dicc)

#Acceder a un valor en un diccionario:

print(dicc["Clave 4"])

#Verificar si una llave existe en un diccionario:

print(dicc.keys())

#Eliminar un elemento de un diccionario:

print(dicc.pop("Clave 1"))

#Imprimir las llaves de un diccionario:

print(dicc.keys())

#Imprimir los valores de un diccionario:

print(dicc.values())

#Imprimir las llaves y valores de un diccionario:

print(dicc.items())
