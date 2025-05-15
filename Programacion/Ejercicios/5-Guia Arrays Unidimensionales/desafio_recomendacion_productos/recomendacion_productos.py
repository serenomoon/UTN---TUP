# Desafío: Sistema de Recomendación de Productos
# Una tienda online quiere mejorar su sistema de recomendaciones analizando el comportamiento de sus clientes. Para ello, dispone del historial de compras de dos usuarios distintos, almacenado en listas de productos.
# 📌 Objetivo: Escribir un programa en Python que permita analizar estos historiales de compra y responder las siguientes preguntas:
#  1️⃣ Productos en común: ¿Qué productos han comprado ambos usuarios?
#  2️⃣ Productos exclusivos: ¿Qué productos ha comprado cada usuario que el otro no ha adquirido?
#  3️⃣ Catálogo total: ¿Cuál sería el conjunto total de productos comprados entre los dos usuarios?
#  4️⃣ Recomendaciones: ¿Cómo podrías utilizar esta información para sugerir productos a cada usuario?
# 🎯 Requisitos:
#  ✔️ El programa debe recibir como entrada dos listas de productos (pueden ser ingresadas manualmente o predefinidas).
#  ✔️ Debe procesar y mostrar los resultados de forma clara.
#  ✔️ Se valorará el uso de funciones para estructurar el código de manera organizada.
# 🔹 Extras opcionales:
# Permitir que los usuarios ingresen sus listas manualmente.
# Ampliar el programa para comparar más de dos usuarios.

import sys
from os import system
import colorama as C
from array_dinamico import agregar_valor_lista
from productos import *



def main() -> None:
    clave_empleados = "12345"
    bandera_empleado = False
    bandera_cliente = False
    bandera_tipo_persona = True

    cliente1 = []
    cliente2 = []
    cliente3 = []

    while bandera_tipo_persona:
        print(C.Fore.BLUE + "1. Ingresar como empleado\n2. Ingresar como cliente\n3. Salir del programa")
        tipo_persona = int(input("Ingresar una opcion: "))
        match tipo_persona:
            case 1:
                clave = input("Ingrese la clave: ")
                if clave == clave_empleados:
                    bandera_empleado = True
            case 2:
                bandera_cliente = True
            case 3:
                bandera_tipo_persona = False
                print("Saliendo del programa...")
        system("cls")


        while bandera_empleado:
            print(C.Fore.BLUE + "1. Productos en común\n2. Productos exclusivos\n3. Catálogo total\n4. Volver al menu principal\n5. Salir del programa")
            opcion_empleado = int(input("Ingresar una opcion: "))
            match opcion_empleado:
                case 1:
                    productos_comun = productos_en_comun(cliente1,cliente2,cliente3)
                    print(f"Los productos en comun de los clientes son: {productos_comun}")
                case 2:
                    producto_exclusivo = productos_exclusivos(cliente1,cliente2,cliente3)
                    print(f"Los productos exclusivos de los clientes son: {producto_exclusivo}")
                case 3:
                    total_productos = productos_totales(cliente1,cliente2,cliente3)
                    print(f"Los productos que llevaron los clientes son: {total_productos}")
                case 4:
                    print("Cerrando sesion...")
                    bandera_empleado = False
                case 5:
                    print("Saliendo del programa...")
                    bandera_empleado = False
                    bandera_tipo_persona = False
            system("pause")
            system("cls")

        while bandera_cliente:
            print("¿Quien es?:\n1- Cliente 1\n2- Cliente 2\n3- Cliente 3")
            numero_cliente = int(input("Ingresar una opcion: "))
            print(C.Fore.BLUE + "1. Ingresar producto\n2. Recomendaciones\n3. Volver al menu principal\n4. Salir del programa")
            opcion_cliente = int(input("Ingresar una opcion: "))
            match opcion_cliente:
                case 1:
                    producto_nuevo = input("Ingrese nuevo producto: ")
                    if numero_cliente == 1:
                        cliente1 = agregar_valor_lista(cliente1,producto_nuevo)
                    elif numero_cliente == 2:
                        cliente2 = agregar_valor_lista(cliente2,producto_nuevo)
                    else:
                        cliente3 = agregar_valor_lista(cliente3,producto_nuevo)
                case 2:
                    print("Productos recomendados para el cliente: ")
                    if numero_cliente == 1:
                        cliente1 = recomendacion(cliente1,cliente2,cliente3)
                        for i in range(len(cliente1)):
                            print(cliente1[i])
                    elif numero_cliente == 2:
                        cliente2 = recomendacion(cliente1,cliente2,cliente3)
                        for i in range(len(cliente2)):
                            print(cliente2[i])
                    else:
                        cliente3 = recomendacion(cliente1,cliente2,cliente3)
                        for i in range(len(cliente3)):
                            print(cliente3[i])
                case 3:
                    print("Cerrando sesion...")
                    bandera_cliente = False
                case 4:
                    print("Saliendo del programa...")
                    bandera_cliente = False
                    bandera_tipo_persona = False
            system("pause")
            system("cls")
    



if __name__ == "__main__":
    sys,exit(main())