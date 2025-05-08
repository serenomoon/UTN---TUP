# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.
i = 0
suma = 0
continuar = 1
while continuar == 1:
    j = int(input(f"Ingrese el {i + 1}° numero: "))
    suma += j
    i += 1
    print(f"Suma de los numeros: {suma}")
    promedio = suma / i
    print(f"Promedio de los numeros: {promedio})")
    print("Desea continuar?")
    continuar = int(input("Ingrese 1 para continuar: "))