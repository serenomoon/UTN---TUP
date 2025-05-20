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

def main() -> None:
    menu_open = True
    vector = []
    while menu_open:
        print("1. Ingresar matriz\n2. Generar matriz aleatoria\n3. Ver cuadrado magico cargado\n4. Salir del programa")
        opcion = int(input("Ingresar una opcion: "))
        match opcion:
            case 1:
                n = int(input("¿Cuando sera el valor de N (N>2) en un cuadrado de NxN?: "))
                vector = ingresar_cuadrado_magico(n)
            case 2:
                vector = generador_cuadrado_magico()
                print("Cuadrado magico generado.")
            case 3:
                if len(vector) < 2:
                    print("No hay un cuadrado magico valido cargado")
                else:
                    mostrar_cuadrado(vector)
            case 4:
                menu_open = False
                print("Saliendo del programa")
        system("pause")
        system("cls")


if __name__ == "__main__":
    sys,exit(main())

