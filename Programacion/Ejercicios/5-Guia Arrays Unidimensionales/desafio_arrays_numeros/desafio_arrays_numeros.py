# 📌 Desafío: Menú de Opciones con Listas y Funciones
# Desarrollar un programa en Python que presente un menú de opciones donde el usuario pueda realizar distintas operaciones con un conjunto de números.
# 🔹 Opciones del Menú:
#  1️⃣ Ingresar datos: Permitir al usuario ingresar 10 números enteros en el rango de -1000 a 1000.
#  2️⃣ Cantidad de positivos y negativos: Mostrar cuántos números ingresados son positivos y cuántos son negativos.
#  3️⃣ Suma de los números pares: Calcular y mostrar la sumatoria de los números pares.
#  4️⃣ Mayor número impar: Identificar y mostrar el mayor número impar ingresado.
#  5️⃣ Listar los números ingresados: Mostrar todos los números en el orden en que fueron ingresados.
#  6️⃣ Listar los números pares: Mostrar únicamente los números pares de la lista.
#  7️⃣ Listar los números en posiciones impares: Mostrar los números que se encuentran en posiciones impares dentro de la lista.
#  8️⃣ Salir del programa.
# 🔹 Condiciones:
#  ✔️ El usuario debe ingresar los números antes de acceder a las opciones 2 a 7.
#  ✔️ El programa debe estar estructurado en funciones, siguiendo el paradigma de programación funcional:
# Funciones específicas: Para operaciones como determinar si un número es positivo, negativo o par.
# Funciones generales: Para listar elementos o calcular sumatorias.
# 🔹 Estructura del Código:
#  📌 El programa debe estar organizado en módulos:
# Especificas.py: Contendrá las funciones específicas.
# Array_Generales.py: Contendrá las funciones generales.
# Las funciones de entrada de datos deben importarse desde el módulo Input.
# 🔹 Consejo:
#  ✅ Desarrollar y probar primero cada función individualmente antes de organizarlas en módulos.


import sys
from os import system
from array_generales import *
from especificas import *
import colorama as C


def main() -> None:
    bandera_menu = True
    bandera_carga = False
    vector = crear_vector(None,10) 
    while bandera_menu:
        print(C.Fore.BLUE + "1. Ingresar Datos\n2. Cantidad de positivos y negativos\n3. Suma de los números pares\n4. Mayor número impar\n5. Listar los números ingresados\n6. Listar los números pares\n7. Listar los números en posiciones impares\n8. Salir del programa")
        opcion = int(input("Ingresar una opcion: "))
        match opcion:
            case 1:
                cargar_lista(vector)
                bandera_carga = True
            case 2:
                if bandera_carga:
                    positivos_negativos(vector)
                else:
                    print("Cargue una lista primero")
            case 3:
                if bandera_carga:
                    sumar_pares = sumar_numeros_pares(vector)
                    print(f"La suma de los numeros pares es: { sumar_pares }")
                else:
                    print("Cargue una lista primero")
            case 4:
                if bandera_carga:
                    mayor_impar = buscar_maximo_impar(vector)
                    if mayor_impar == None:
                        print("No hay ningun impar en la lista")
                    else:
                        print(f"El mayor numero impar es: {mayor_impar}")
                else:
                    print("Cargue una lista primero")
            case 5:
                if bandera_carga:
                    mostrar_lista(vector)
                else:
                    print("Cargue una lista primero")
            case 6:
                if bandera_carga:
                    lista_pares = lista_numeros_pares(vector)
                    print(f"Los numeros pares de la lista son: {lista_pares}")
                else:
                    print("Cargue una lista primero")
            case 7:
                if bandera_carga:
                    posiciones_impares = lista_numeros_posiciones_impares(vector)
                    print(f"Los numeros en posiciones imapares de la lista son: {posiciones_impares}")
                else:
                    print("Cargue una lista primero")
            case 8:
                print("Saliendo del programa...")
                bandera_menu = False
        system("pause")
        system("cls")



if __name__ == "__main__":
    sys,exit(main())