lista = [None] * 20
seguir = "si"

while seguir == "si":
    numero = int(input("Ingrese un numero: "))
    posicion = int(input("Ingrese posicion: "))
    while posicion < 1 or posicion > len(posicion):
        posicion = int(input("Reingrese posicion: "))

    if lista[posicion-1] == None:
        lista[posicion-1] = numero
    else:
        print("La posicion ya esta ocupada")

    seguir = input("Ingresar otro si/no?: ")

for i in range(len(lista)):
    if lista[i] != None:
        print(lista[i])