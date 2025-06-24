# txt
# csv
# json

# archivo = open("nombre.txt","w") # Abrir o generar un el archivo rwa (ver, escribir y agregar)
# # Si el archivo no existe lo crea, si existe lo sobreescribe

# archivo.write("Saulo") # Escribimos pasandole cadena o variable (Sobreescribiendo lo que ya estaba)

# archivo.close() # Cerramos el archivo


# archivo = open("nombre.txt","a") # Append para no sobreescribir

# archivo.write(" Fernandez")

# archivo.close() # Cerramos el archivo


# LEER ARCHIVO
# archivo = open("nombre.txt","r") # el parametro r viene por defecto, no hace falta ponerlo (igual ponerlo)
# Puedo leer por lineas o todo el archivo

# contenido = archivo.read() # Lee todo el archivo
# contenido = archivo.readline() # Lee una linea
# contenido2 = archivo.readline() # Lee la siguiente
# contenido = archivo.readlines() # Leo todas las lineas en una lista, guarda los saltos de linea

# archivo.close()
# print(contenido)
# print(contenido2)

# Si hago print me va a salir con salto de linea
# for texto in contenido:
#     print(texto)

# Creamos una lista y la guardamos
# lista = ["Superman", "Spiderman", "Batman", "Goku"]
# with open("lista_super.txt","w") as archivo: # Con white no necesito hacer close
#     for heroe in lista:
#         archivo.write(f"{heroe}\n")

# with open("lista_super.txt","r") as archivo:
#     lista = archivo.readlines()

# for heroe in lista:
#     print(heroe)


# Iterar archivo
# with open("lista_super.txt","r") as archivo:
#     for linea in archivo:
#         print(linea)



# csv = Comma separated values
# nombres = ["Luis", "Maria", "Juan"]
# apellidos = ["Gonzalez", "Ruiz", "Gomez"]
# edades = [23,33,44] # Se guardan en str

# with open("agenda.csv","w") as archivo:
#     for i in range(len(nombres)):
#         registro = f"{nombres[i]},{apellidos[i]},{edades[i]}\n"
#         archivo.write(registro)


# Leemos el archivo
import re # Regular expression

# with open("agenda.csv","r") as archivo:
#     for linea in archivo:
#         # lista = linea.split(",") # Buscamos el caracter y la sacamos, añadimos datos a la lista
#         lista = re.split(",|\n", linea) # Recibe dos o mas datos y la linea que quiero splitear
#         print(f"{lista[0]} - {lista[1]} - {lista[2]}")


# PARSERS
# def parser_csv(path) -> list:
#     lista_nueva = []
    
#     with open(path,"r", encoding= "utf8") as archivo: # Le agregamos el conjunto de caracteres a usar
#         archivo.redline() # Para leer la primer linea (titulos) y no tener error con int(DNI)
#         for linea in archivo:
#             diccionario = {}
#             lista = re.split(",|\n", linea)
#             diccionario["Autorizado"] = lista[0]
#             diccionario["DNI"] = int(lista[1])
#             diccionario["Apellido_Nombre"] = f"{lista[2]} {lista[3]}"
#             diccionario["Fecha"] = lista[7]

#             lista_nueva.append(diccionario)
#     return lista_nueva

# lista_empleados = parser_csv("personal.csv")
# for empleado in lista_empleados:
#     print(empleado)


# JSON 
def parser_csv(path) -> list:
    lista_nueva = []
    
    with open(path,"r", encoding= "utf8") as archivo: # Le agregamos el conjunto de caracteres a usar
        archivo.redline() # Para leer la primer linea (titulos) y no tener error con int(DNI)
        for linea in archivo:
            diccionario = {}
            lista = re.split(",|\n", linea)
            diccionario["ID"] = lista[0]
            diccionario["Nombre"] = lista[1]
            diccionario["Apellido"] = lista[2]
            diccionario["Sueldo"] = float(lista[3])

            lista_nueva.append(diccionario)
    return lista_nueva

lista_empleados = parser_csv("personal.csv")
nueva = []
for empleado in lista_empleados:
    if empleado["Sueldo"] > 2000:
        nueva.append(empleado)

import json

with open("filtro.json", "w") as archivo:
    json.dump(nueva,archivo, indent=4) # Dump para escribir, indent para que quede mejor iterado el json

with open("filtro.json", "r") as archivo:
    empleados = json.load(archivo) # Para leer
