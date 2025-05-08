# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.
i = 0
positivos = 0
negativos = 1
continuar = 1
while continuar == 1:
        j = int(input(f"Ingrese el {i + 1}° numero: "))
        if j > 0:
            positivos += j
            i += 1
        elif j < 0:
            negativos *= j
            i += 1
        else:
            print("El seleccion ingresada es incorrecta.")
            continuar == 0
        print("Desea continuar?")
        continuar = int(input("Ingrese 1 para continuar: "))
print(f"Suma de los numeros: {positivos}")
print(f"Producto de los numeros: {negativos}")