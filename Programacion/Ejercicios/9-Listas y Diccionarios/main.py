# Playlist de Lady Gaga - Gestor de Videos en YouTube 🎶
# Lady Gaga es una de las artistas más influyentes del pop, con una extensa lista de reproducciones en YouTube. 
# Para facilitar el análisis y manipulación de su contenido, desarrollaremos un software que permita gestionar su lista de videos.
# A través de un menú interactivo, los usuarios podrán visualizar, ordenar, buscar y analizar la información de cada video de la lista.
# 📌 Funcionalidades del Software
# 🔹 1. Normalización de Datos
# El formato original de los datos no está estandarizado, por lo que se deben normalizar utilizando funciones preexistentes. 
# Cada video deberá contener la siguiente información correctamente estructurada:
# Título (str): Nombre del tema.
# Colaboradores (list): Lista de artistas invitados (si los hay).
# Vistas (int): Cantidad de reproducciones en números enteros.
# Duración (int): Duración del video en segundos.
# Link (str): Enlace directo al video en YouTube.
# Fecha de lanzamiento (date): Fecha de publicación del video.
# 🔹 2. Mostrar Lista de Temas
# Se presentará la lista de todos los temas en formato tabular. 
# No es necesario mostrar todos los datos, solo los esenciales (por ejemplo, título y duración).
# 🔹 3. Ordenar Temas
# Los videos se ordenarán por duración, de mayor a menor.
# 🔹 4. Promedio de Vistas
# Se calculará y mostrará el promedio de vistas de todos los videos en millones.
# 🔹 5. Máxima Reproducción
# Se listará el video (o los videos) con la mayor cantidad de vistas.
# 🔹 6. Mínima Reproducción
# Se listará el video (o los videos) con la menor cantidad de vistas.
# 🔹 7. Búsqueda por Código
# El usuario ingresará un código de video y el programa mostrará todos los detalles asociados a ese video.
# 🔹 8. Listar por Colaborador
# El usuario ingresará el nombre de un colaborador (de una lista de colaboradores existentes) 
# y el programa mostrará todos los videos en los que haya participado.
# 🔹 9. Listar por Mes de Lanzamiento
# El usuario ingresará un mes y se listarán todos los temas lanzados en ese mes, sin importar el año.
# 🔹 10. Salir
# Finalizar la ejecución del programa.
# 📌 Requisitos del Desarrollo
# ✅ Estructura Modular: Cada funcionalidad deberá estar programada en funciones específicas para facilitar la reutilización del código.
# ✅ Manejo de Datos: Validar correctamente los formatos de entrada y realizar conversiones cuando sea necesario.
# ✅ Interfaz Clara: Los menús y las opciones deberán ser intuitivos y fáciles de usar.
# ✅ Optimización de búsquedas: Garantizar eficiencia en las consultas sobre la lista de videos.

import sys
from os import system
from funciones import *
from lady_gaga import *

def main():
    menu_open = True
    datos_normalizados = []
    while menu_open:
        print("Bienvenido al fan club de Lady Gaga")
        opcion = int(input("MENU:\n" \
        "1. Normalización de Datos\n" \
        "2. Mostrar Lista de Temas\n" \
        "3. Ordenar Temas\n" \
        "4. Promedio de Vistas\n" \
        "5. Máxima Reproducción\n" \
        "6. Mínima Reproducción\n" \
        "7. Búsqueda por Código\n" \
        "8. Listar por Colaborador\n" \
        "9. Listar por Mes de Lanzamiento\n" \
        "10. Salir\n" \
        "Elige una opcion: "))
        match opcion:
            case 1:
                datos_normalizados = normalizar_datos(playlist_lady_gaga)
                print("Los datos fueron normalizados con exito.")
            case 2:
                if len(datos_normalizados) > 1:
                    mostrar_temas(datos_normalizados)
                else:
                    print("Primero normalice los datos.")
            case 3:
                if len(datos_normalizados) > 1:
                    ordenar_por_duracion(datos_normalizados)
                    print("Las canciones se ordenaron por duracion.")
                else:
                    print("Primero normalice los datos.")
            case 4:
                if len(datos_normalizados) > 1:
                    promedio = promedio_vistas_millones(datos_normalizados)
                    print(f"Promedio de vistas: {promedio:.2f} millones")
                else:
                    print("Primero normalice los datos.")
            case 5:
                if len(datos_normalizados) > 1:
                    videos = videos_max_min(datos_normalizados)
                    print("Videos con mas reproducciones:")
                    for video in videos:
                        print(f"{video['Título']} con {video['Vistas']:,} vistas")
                else:
                    print("Primero normalice los datos.")
            case 6:
                if len(datos_normalizados) > 1:
                    videos = videos_max_min(datos_normalizados, 'min')
                    print("Videos con menos reproducciones:")
                    for video in videos:
                        print(f"{video['Título']} con {video['Vistas']:,} vistas")
                else:
                    print("Primero normalice los datos.")
            case 7:
                if len(datos_normalizados) > 1:
                    codigo = input("Ingrese codigo del video: ")
                    resultado = buscar_video_por_codigo(datos_normalizados, codigo)
                    if resultado:
                        print("Video encontrado:")
                        for video in resultado:
                            print(f"{video}: {resultado[video]}")
                    else:
                        print("No se encontró video con ese código.")
                else:
                    print("Primero normalice los datos.")
            case 8:
                if len(datos_normalizados) > 1:
                    colaborador = input("Ingrese nombre del colaborador: ")
                    videos = listar_videos_por_colaborador(datos_normalizados, colaborador)
                    if videos:
                        print(f"Videos con colaborador '{colaborador}':")
                        for video in videos:
                            print(f"{video['Título']} (Vistas: {video['Vistas']:,})")
                    else:
                        print(f"No se encontraron videos con el colaborador '{colaborador}'.")
                else:
                    print("Primero normalice los datos.")
            case 9:
                if len(datos_normalizados) > 1:
                    mes = int(input("Ingrese número del mes (1-12): "))
                    if mes:
                        mes = int(mes)
                        if 1 <= mes <= 12:
                            videos = listar_videos_por_mes(datos_normalizados, mes)

                            if videos:
                                print(f"Videos lanzados en el mes {mes}:")
                                for v in videos:
                                    print(f"{v['Título']} (Fecha: {v['Fecha de lanzamiento'].strftime('%Y-%m-%d')})")
                            else:
                                print(f"No se encontraron videos lanzados en el mes {mes}.")
                        else:
                            print("Número de mes inválido. Debe estar entre 1 y 12.")
                    else:
                        print("Entrada inválida. Ingrese un número.")
                else:
                    print("Primero normalice los datos.")
            case 10:
                print("Saliendo del programa...")
                menu_open = False
        system("pause")
        system("cls")



if __name__ == "__main__":
    sys.exit(main())