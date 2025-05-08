# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
# A-La suma acumulada de los números negativos.
# B-La suma acumulada de los números positivos.
# C-La cantidad de números negativos ingresados.
# D-El promedio de los números positivos.
# E-El número positivo más grande.
# F-El porcentaje de números negativos ingresados, respecto del total de ingresos.
i = 0
positivos = 0
negativos = 0
cantidad_positivos = []
cantidad_negativos = 0
continuar = 1
while continuar == 1:
        j = int(input(f"Ingrese el {i + 1}° numero: "))
        if j > 0:
            positivos += j
            cantidad_positivos.append(j)
            i += 1
        elif j < 0:
            negativos += j
            cantidad_negativos += 1
            i += 1
        else:
            continuar == 0
        print("Desea continuar?")
        continuar = int(input("Ingrese 1 para continuar: "))

if i > 0:
    print(f"Suma de los numeros negativos: {negativos}")
    print(f"Suma de los numeros positivos: {positivos}")
    print(f"Cantidad de numeros negativos ingresados: {cantidad_negativos}")
    if len(cantidad_positivos) > 0 : 
        promedio = positivos / len(cantidad_positivos)
        maximo_positivo = max(cantidad_positivos)
        print(f"Promedio positivos: {promedio}")
        print(f"Numero mas alto de los positivos: {maximo_positivo}")
    else:
        print("No se ingresaron numeros positivos")
    porcentaje_negativos = (cantidad_negativos / i) * 100
    print(f"Porcentaje de numeros negativos ingresados: {porcentaje_negativos}")