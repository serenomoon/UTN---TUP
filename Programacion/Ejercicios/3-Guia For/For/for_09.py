# Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.
cantidad_divisores = 0
numero_ingresado = int(input("Ingrese un numero: "))
for i in range(1,numero_ingresado+1):
    if numero_ingresado % i == 0:
        cantidad_divisores += 1
        print(f"{i} es divisor de {numero_ingresado}")
print(f"Cantidad de divisores: {cantidad_divisores}")