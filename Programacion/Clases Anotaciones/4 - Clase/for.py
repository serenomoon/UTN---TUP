# rango = range(5)
# print(list(rango))

# rango = range(5) hasta e inicia en 0
# rango = range(5,10) desde/hasta e inicia en 5
# rango = range(5,10,3) desde/hasta y el incremento

# contador2 = 0
# while contador2 < 10:
#     print(contador2 + 1)
#     contador2 += 1

# # El while es igual al siguiente for:
# for contador in range(10):
#     print(contador + 1)
# # O
# for contador in range(11):
#     print(contador)


# for i in range(10,0,-1):
#     print(i)

# Ingresar hasta 20 numeros o hasta encontrarnos con un multiplo de 5
# for i in range(20):
#     numero = int(input(f"Ingresar {i + 1}° numero: "))
#     if numero % 5 == 0:
#         print("Numero es multiplo de 5")
#         break

# Ingresar hasta 10 numeros, mostrar solo pares
# for i in range(10):
#     numero = int(input(f"Ingresar {i + 1}° numero: "))
#     if numero % 2 == 0:
#         print(f"Numero es par: {numero}")

# Lo mismo pero usando el continue:
# for i in range(10):
#     numero = int(input(f"Ingresar {i + 1}° numero: "))
#     if numero % 2 != 0:
#         continue #Fuerza a cortar y continuar con siguiente iteracion, el break corta todo
#     print(f"Numero es par: {numero}")

# print("hola", end = "-") #Finaliza con un guion en vez de con un salto
# print("chau")

# for anidado
# for i in range(5): #5
#     print(f"{i}")
#     for j in range(3): #15
#         print(f"\t{j}")


# For primos:

# numero = 23
# bandera_primo = False
# for i in range(2, numero): #en vez de poner 1 y el mismo numero pongo los intermedios (ya se q 1 y el mismo es divisible)
#     if numero % i == 0:
#         bandera_primo = True
#         break

# if bandera_primo == True:
#     print("El numero No es primo")
# else:
#     print("El numero es primo")


# todos los primos entre el 1 y el ingresado

numero = 7
contador = 0
for i in range(2, numero + 1): 
    bandera = False
    for j in range(2, i): 
        if i % j == 0:
            bandera = True
            break
    if bandera == False:
        print(i) #es primo
        contador += 1

print(f"Cantidad de numeros primos: {contador}")

