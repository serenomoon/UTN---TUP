# Playlist de Lady Gaga - Gestor de Videos en YouTube 🎶
# Lady Gaga es una de las artistas más influyentes del pop, con una extensa lista de reproducciones en YouTube. Para facilitar el análisis y manipulación de su contenido, desarrollaremos un software que permita gestionar su lista de videos.
# A través de un menú interactivo, los usuarios podrán visualizar, ordenar, buscar y analizar la información de cada video de la lista.
# 📌 Funcionalidades del Software
# 🔹 1. Normalización de Datos
# El formato original de los datos no está estandarizado, por lo que se deben normalizar utilizando funciones preexistentes. Cada video deberá contener la siguiente información correctamente estructurada:
# Título (str): Nombre del tema.
# Colaboradores (list): Lista de artistas invitados (si los hay).
# Vistas (int): Cantidad de reproducciones en números enteros.
# Duración (int): Duración del video en segundos.
# Link (str): Enlace directo al video en YouTube.
# Fecha de lanzamiento (date): Fecha de publicación del video.
# 🔹 2. Mostrar Lista de Temas
# Se presentará la lista de todos los temas en formato tabular. No es necesario mostrar todos los datos, solo los esenciales (por ejemplo, título y duración).
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
# El usuario ingresará el nombre de un colaborador (de una lista de colaboradores existentes) y el programa mostrará todos los videos en los que haya participado.
# 🔹 9. Listar por Mes de Lanzamiento
# El usuario ingresará un mes y se listarán todos los temas lanzados en ese mes, sin importar el año.
# 🔹 10. Salir
# Finalizar la ejecución del programa.
# 📌 Requisitos del Desarrollo
# ✅ Estructura Modular: Cada funcionalidad deberá estar programada en funciones específicas para facilitar la reutilización del código.
# ✅ Manejo de Datos: Validar correctamente los formatos de entrada y realizar conversiones cuando sea necesario.
# ✅ Interfaz Clara: Los menús y las opciones deberán ser intuitivos y fáciles de usar.
# ✅ Optimización de búsquedas: Garantizar eficiencia en las consultas sobre la lista de videos.

from os import sys

def main():
    menu_open = True
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
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                print("Saliendo del programa...")
                menu_open = False



if __name__ == "__main__":
    sys.exit(main())