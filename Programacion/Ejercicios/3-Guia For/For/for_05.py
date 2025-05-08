# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
suma_numeros = 0
cantidad_numeros = 0

for i in range(10):
    numero_ingresado = int(input("Ingrese un numero: "))
    if numero_ingresado == 0:
        break
    suma_numeros += numero_ingresado
    cantidad_numeros += 1

if cantidad_numeros > 0:
    promedio_numeros = suma_numeros / cantidad_numeros
    print(f"Suma de los numeros: {suma_numeros}")
    print(f"Promedio de los numeros: {promedio_numeros}")
else:
    print("No se ingresaron numeros")