# 📌 Desafío: Gestión de Recaudaciones en una Empresa de Colectivos
# Una empresa de transporte cuenta con 3 líneas de colectivos, cada una con 5 coches, lo que da un total de 15 unidades en circulación. 
# La empresa emplea 15 choferes, cada uno identificado con un legajo único generado aleatoriamente.
# Para llevar un control eficiente de la recaudación diaria, se necesita desarrollar un software que permita gestionar y analizar 
# los ingresos obtenidos por cada línea y coche.

# 🔹 Funcionalidades del Programa
# El sistema debe presentar un menú de opciones con las siguientes funciones:
# 1️⃣ Cargar planilla de recaudación
# El chofer debe identificarse ingresando su número de legajo.
# Se debe validar que el legajo ingresado exista dentro de la matriz de legajos generada previamente.
# Si el chofer existe, podrá ingresar la recaudación indicando la línea y el coche en el que realizó el viaje.
# Un chofer puede cargar múltiples recaudaciones por día, en distintas líneas y coches.
# Cada coche dentro de cada línea puede acumular varias recaudaciones diarias.
# 2️⃣ Mostrar la recaudación de cada coche y línea
# Presentar una matriz con la recaudación total de cada coche en cada línea.
# 3️⃣ Calcular y mostrar la recaudación por línea
# Sumar y mostrar la recaudación total de cada línea de colectivos.
# 4️⃣ Calcular y mostrar la recaudación por coche
# Permitir al usuario seleccionar un coche y mostrar la suma total de su recaudación.
# 5️⃣ Calcular y mostrar la recaudación total
# Mostrar el total general de todas las recaudaciones registradas.
# 6️⃣ Salir del programa


# 🔹 Requisitos del Desarrollo
# ✔️ Modularización:
# El programa debe estar organizado en múltiples funciones, incluyendo:
# Ingreso de datos
# Validación de líneas y coches
# Generación y verificación de existencia de legajo
# Cálculos de recaudaciones
# ✔️ Validaciones:
# El legajo ingresado debe existir en la matriz de legajos.
# La línea y el coche seleccionados deben ser válidos.
# No debe permitirse el ingreso de valores negativos o inválidos en la recaudación.
import sys
from os import system
from funciones_desafio_colectivos import *


def main() -> None:
    menu_colectivos = True
    colectivos = crear_linea_y_coches(None,5,3)
    choferes = crear_choferes(15)
    recaudacion = crear_matriz(0,5,3)
    print(choferes)
    while menu_colectivos:
        opcion = int(input("Colectivos 'El Coletivo':\n1- Cargar planilla de recaudacion\n2- Ver recaudacion de coches y lineas\n3- Ver recaudacion por linea\n4- Ver recaudacion por coche\n5- Ver recaudacion total\n6- Salir del programa\nIngresar una opcion: "))
        match opcion:
            case 1:
                ingresando = True
                numero_legajo = int(input("Ingrese su numero de legajo: "))
                if confirmar_legajo(numero_legajo, choferes):
                    while ingresando:
                        system("cls")
                        print("Lineas:")
                        mostrar_matriz(colectivos)
                        numero_linea = int(input("Ingrese el numero de linea a la que quiere acceder: "))
                        system("cls")
                        while not confirmar_coche(numero_linea,colectivos):
                            reingreso = int(input("Numero de linea no valido\n1- Reingresar\n2- Volver\nDesea reingresarlo o volver al menu?: "))
                            system("cls")
                            if reingreso == 1:
                                print("\tLineas:")
                                mostrar_matriz(colectivos)
                                numero_linea = int(input("Reingrese el numero: "))
                            else:
                                print("Volviendo al menu...")
                                system("cls")
                                ingresando = False
                                break
                        if confirmar_coche(numero_linea,colectivos):
                            recaudo = int(input(f"Ingrese cuando recaudo en el coche N°{numero_linea}: "))
                            recaudacion = carga_racaudacion(recaudo, numero_linea, colectivos, recaudacion)
                            print("Recaudacion agregada")
                            continuar_ingresando = int(input("Seleccione:\n1- Agregar otra recaudacion\n2- Volver al menu\nIngrese una opcion: "))
                            if continuar_ingresando == 2:
                                ingresando = False
                else:
                    print("Numero de legajo incorrecto, volviendo al Menu...")
            case 2:
                system("cls")
                print("Recaudacion de coches:\n")
                mostrar_recaudacion_coche(colectivos,recaudacion)
            case 3:
                system("cls")
                print("Recaudacion de lineas:\n")
                mostrar_recaudacion(colectivos,recaudacion)
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("Saliendo del programa...")
                menu_colectivos = False
        system("pause")
        system("cls")


if __name__ == "__main__":
    sys.exit(main())