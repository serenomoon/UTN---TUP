# 📌 Desafío: Verificación de un Cuadrado Mágico
# Un cuadrado mágico es una matriz cuadrada de n × n en la que la suma de los números en cada fila, 
# cada columna y cada diagonal principal es la misma. Esta suma se conoce como constante mágica (M), y 
# se calcula con la siguiente fórmula:

# M = (n*(n**2+1))/2

# Formalmente, un cuadrado mágico de orden n contiene los números enteros del 1 al n², organizados de 
# manera que cumplen la condición de igualdad en las sumas.

# 🔹 Objetivo
# Desarrollar un programa en Python que permita ingresar una matriz cuadrada de orden n y determine si 
# es un cuadrado mágico.

# 🔹 Requisitos del Programa
# ✔️ Ingreso de datos:
# Permitir que el usuario ingrese la matriz manualmente o, de manera opcional, generar una aleatoria.
# Validar que los valores ingresados sean números enteros en el rango de 1 a n² y que no se repitan.
# Asegurar que la matriz ingresada tenga un tamaño válido (n × n).


# ✔️ Verificación del cuadrado mágico:
# Calcular la constante mágica según la fórmula.
# Comparar la suma de:
# Cada fila
# Cada columna
# Las dos diagonales principales
# Determinar si todas las sumas son iguales a la constante mágica.
# ✔️ Salida de resultados:
# Mostrar la matriz ingresada de forma clara y organizada.
# Indicar si la matriz es un cuadrado mágico o no.



# 📌 Extras opcionales:
#  ✅ Permitir que el usuario ingrese matrices de distintos tamaños (por ejemplo, 3×3, 4×4, etc.).
#  ✅ Mostrar mensajes de error en caso de ingreso inválido.
#  ✅ Implementar una opción para generar un cuadrado mágico válido automáticamente.

import sys
from os import system
from funciones_cuadrado_magico import *
# 3x3
# n = 4
# M = (n*(n**2+1))/2
# print(f"M de {n}x{n} es: {M}")
# 1 = 1
# 2 = 5
# 3 = 15
# 4 = 34
# 5 = 65
# 6 = 111

# 2x2 no verifica
matriz2x2 = [
    [2,4],
    [1,3],
]

matriz3x3 = [
    [2,7,6],
    [9,5,1],
    [4,3,8]
]

matriz4x4 = [
    [16, 3, 2,13],
    [ 5,10,11, 8],
    [ 9, 6, 7,12],
    [ 4,15,14, 1],
]

def main() -> None:
    menu_open = True
    while menu_open:
        print("1. Ingresar matriz\n2. Generar matriz aleatoria\n3. Es un cuadrado magico?\n4. Salir del programa")
        opcion = int(input("Ingresar una opcion: "))
        match opcion:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                menu_open = False
                print("Saliendo del programa")
        system("cls")


# test = matriz4x4

# suma_hori = suma_horizontal(test)
# print(f"Suma horizontal: {suma_hori}")
# suma_verti = suma_vertical(test)
# print(f"Suma vertical: {suma_verti}")
# suma_diago = suma_diagonal(test)
# print(f"Suma diagonal: {suma_diago}")
# suma_diago_inver = suma_diagonal_invertida(test)
# print(f"Suma diagonal invertida: {suma_diago_inver}")

# es_magikh = verificar_cuadrado_magico(test)
# print(f"La matriz es un cuadrado magico: {es_magikh}")


if __name__ == "__main__":
    sys,exit(main())

# print(M)