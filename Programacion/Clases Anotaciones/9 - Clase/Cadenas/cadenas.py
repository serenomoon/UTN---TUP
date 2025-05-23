cadena = "CASA" #Se puede descomponer en caracateres, es un elemento iterable
# cadena[1] seria "A"

contador_A = 0
for i in range(len(cadena)):
    if cadena[i] == "A":
        contador_A += 1

print(contador_A) #Cuantas A tiene CASA

cadena2 = "Casa"
# cadena2[2] = "P" #No puedo porque es inmutable
# Tendria que crear una cadena auxiliar y usar += para ir agregando

cadena_auxiliar = ""
for i in range(len(cadena2)):
    if cadena2[i] == "a":
        cadena_auxiliar += "p"
    else:
        cadena_auxiliar += cadena2[i]
print(cadena_auxiliar)
 

# Ahora juntamos 2 strings en una variable:
nombre = "Juan"
apellido = "Gomez"

nombre_completo = apellido + ", " + nombre
nombre_completo2 = f"{apellido}, {nombre}" # Interpolado de variables
print(nombre_completo)
print(nombre_completo2)


# Comparamos para mostrar bool

cadena = "hola"

print(cadena == "hola") 
# Muestra True

print(cadena < "Hola") 
# Muestra False porque alfabeticamente hola esta despues que Hola, en la tabla ASCII
# Porque el codigo de H > h

print(cadena > "Zorro")
# Muestra False porque compara la primer letra, y Z > h


# entre una minuscula y una mayuscula hay 32 numeros de diferencia en la tabla ASCII:
A = 65 # Numero binario que se pasa a memoria para saber que es una A
a = 97 # 32 bits de diferencia

B = 66
b = 98

# 65 al 90 letras mayusculas
# 91 al 122 letras minusculas
# etc...

print(ord("H")) # Me muestra el caracter en numero binario segun el codigo ASCII

print(ord("H") + 32) # Me da el valor binario de "h"

ascii_caracter = ord("H") + 32
caracter = chr(ascii_caracter) #chr pasa de binario a str
print(caracter)


# Iteramos la cadena y la pasamos a minuscula:
cadena_mayuscula = "HOLA"
cadena_minuscula = ""
for i in range(len(cadena_mayuscula)):
    ascii_caracter = ord(cadena_mayuscula[i]) + 32
    caracter = chr(ascii_caracter) 
    cadena_minuscula += caracter
print(cadena_minuscula)


# Que pasa si la cadena no tiene solo caracteres de letras?
cadena_con_mas_caracteres = "HOLA COMO ESTAN TODOS?? <3"
cadena_con_mas_caracteres_cambiada = ""
# for i in range(len(cadena_con_mas_caracteres)):
#     ascii_caracter = ord(cadena_con_mas_caracteres[i])
#     if ascii_caracter >= 65 and ascii_caracter <= 90: # Buscamos que este entre el rango de las mayusculas
#         caracter = chr(ascii_caracter + 32) # Si esta le sumamos 32 para convertirla a minuscula
#         cadena_con_mas_caracteres_cambiada += caracter # La agregamos a la nueva cadena
#     else:
#         cadena_con_mas_caracteres_cambiada += cadena_con_mas_caracteres[i] # Si no esta en el rango de mayusculas la agregamos sin modificar
# print(cadena_con_mas_caracteres_cambiada)

#Forma mejorada:
for i in range(len(cadena_con_mas_caracteres)):
    caracter = cadena_con_mas_caracteres[i]
    orden = ord(caracter)
    if orden >= 65 and orden <= 90: 
        conversion = orden + 32
        caracter = chr(conversion)
    cadena_con_mas_caracteres_cambiada += caracter

print(cadena_con_mas_caracteres_cambiada)


# OTRA FORMA:

def buscar_caracter(caracater_busqueda: str, caracteres_validos: str):
    encontro = False
    for i in range(len(caracteres_validos)):
        if caracater_busqueda == caracteres_validos[i]:
            encontro = True
            break
    return encontro

cadena = "HOLa"
cadena_minuscula = ""
caracteres_validos = "ABCDEFGHIJKLMNÑOPQRSTUXYZ"

for i in range(len(cadena)):
    caracter = cadena[i]
    if buscar_caracter(caracter, caracteres_validos):
        conversion = ord(caracter) + 32
        caracter = chr(conversion)
    cadena_minuscula += caracter

print(cadena_minuscula)




