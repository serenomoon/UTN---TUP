# contador = 0
# maximo = float("-inf")
# minimo = float("inf")

# maximo = -10000000000
# minimo = 10000000000

# while contador < 5:
#     numero = int(input("Ingrese un numero: "))
#     if numero > maximo:
#         maximo = numero

#     if numero < minimo:
#         minimo = numero
    
#     contador += 1

# print(f"Maximo: {maximo}")
# print(f"Minimo: {minimo}")



# SEGUNDA SOLUCION
# contador = 0
# numero = int(input("Ingrese un numero: ")) # Pido el primer numero fuera y lo tomo como max y min

# maximo = numero
# minimo = numero

# while contador < 4:
#     numero = int(input("Ingrese un numero: "))
#     if numero > maximo:
#         maximo = numero

#     if numero < minimo:
#         minimo = numero
    
#     contador += 1

# print(f"Maximo: {maximo}")
# print(f"Minimo: {minimo}")



# TECERA SOLUCION
# contador = 0

# while contador < 5:
#     numero = int(input("Ingrese un numero: "))
#     if contador == 0:
#         maximo = numero
#         minimo = numero

#     if numero > maximo:
#         maximo = numero

#     if numero < minimo:
#         minimo = numero
    
#     contador += 1

# print(f"Maximo: {maximo}")
# print(f"Minimo: {minimo}")



# CUARTA SOLUCION
# contador = 0

# while contador < 5:
#     numero = int(input("Ingrese un numero: "))
#     if contador == 0 or numero > maximo:
#         maximo = numero
#     if contador == 0 or numero < minimo:
#         minimo = numero
    
#     contador += 1

# print(f"Maximo: {maximo}")
# print(f"Minimo: {minimo}")



# QUINTA SOLUCION
# contador = 0
# maximo = 0
# minimo = 0

# while contador < 5:
#     numero = int(input("Ingrese un numero: "))
#     if  numero > maximo or contador == 0:
#         maximo = numero
#     if  numero < minimo or contador == 0:
#         minimo = numero
    
#     contador += 1

# print(f"Maximo: {maximo}")
# print(f"Minimo: {minimo}")



# SEXTA SOLUCION
seguir = "si" #OPCION CON FLAG
maximo = 0
minimo = 0
bandera_primer_ingreso = False

while seguir == "si":
    numero = int(input("Ingrese un numero: "))
    if  numero > maximo or bandera_primer_ingreso == False:
        maximo = numero
    if  numero < minimo or bandera_primer_ingreso == False:
        minimo = numero

        bandera_primer_ingreso = True

    seguir = input("Continuar? ")

print(f"Maximo: {maximo}")
print(f"Minimo: {minimo}")