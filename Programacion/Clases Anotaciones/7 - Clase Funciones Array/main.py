import sys
from os import system
from funcion_array import *
import colorama as C

def main() -> None:
    bandera_menu = True
    bandera_carga = False
    vector = crear_vector(None,5) 
    while bandera_menu:
        print(C.Fore.BLUE + "1. Cargar\n2. Mostrar\n3. Buscar max\n4. Buscar posiciones max\n5. Hay pares?\n6. Salir")
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                cargar_lista(vector, "Ingrese un numero: ")
                bandera_carga = True
            case 2:
                if bandera_carga:
                    mostrar_lista(vector)
                else:
                    print("Cargue una lista primero")
            case 3:
                if bandera_carga:
                    maximo = buscar_maximo(vector)
                    print(f"El maxmimo es: {maximo}")
                else:
                    print("Cargue una lista primero")
            case 4:
                if bandera_carga:
                    maximo = buscar_maximo(vector)
                    mostrar_posiciones_valor(vector, maximo)
                else:
                    print("Cargue una lista primero")
            case 5:
                if bandera_carga:
                    if buscar_numero_par(vector):
                        print("Por lo menos hay un numero par")
                    else:
                        print("No ingreso ningun numero par")
                else:
                    print("Cargue una lista primero")
            case 6:
                print("Saliendo del programa...")
                bandera_menu = False
        # input("") Esto o:
        system("pause")
        system("cls")



if __name__ == "__main__":
    sys,exit(main())