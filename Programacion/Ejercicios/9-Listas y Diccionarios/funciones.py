from lady_gaga import playlist_lady_gaga
from funciones_generales import *

def mostrar_playlist(playlist: dict) -> None:
    print(f"Titulo: {obtener_nombre_tema(playlist["Tema"]):<15}", end = "")
    print("")

def mostrar_datos(playlist: list) -> None:
    for temas in playlist:
        mostrar_playlist(temas)

# mostrar_datos(playlist_lady_gaga)
mostrar_datos(playlist_lady_gaga)

# Título (str): Nombre del tema.
# Colaboradores (list): Lista de artistas invitados (si los hay).
# Vistas (int): Cantidad de reproducciones en números enteros.
# Duración (int): Duración del video en segundos.
# Link (str): Enlace directo al video en YouTube.
# Fecha de lanzamiento (date): Fecha de publicación del video.
