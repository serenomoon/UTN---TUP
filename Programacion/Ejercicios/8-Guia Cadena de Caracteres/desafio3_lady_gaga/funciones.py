from datetime import date
from datos import *

def obtener_colaboradores(titulo: str) -> list:
    colaboradores_recortados = titulo.split("-")[0]
    nueva_lista = []
    for i in range(len(colaboradores_recortados.split("|"))):
        nuevo = colaboradores_recortados.split("|")[i].strip()
        nueva_lista.append(nuevo)
    return nueva_lista
    # Recibe como parámetro el título del tema.
    # Retorna una lista con los colaboradores (excluyendo el nombre del tema).

def obtener_nombre_tema(titulo: str) -> str:
    return titulo.split("-")[1].strip()
    # Recibe el título del tema.
    # Retorna el nombre real del tema, eliminando a los colaboradores.

def convertir_vistas_numerico(vistas: str) -> int:
    numeros = int(vistas.split(" ")[0])
    letras = vistas.split(" ")[1]
    
    if letras == "millones":
        numeros = numeros*1_000_000
    elif letras == "mil":
        numeros = numeros*1_000
    return numeros
    # Convierte la cantidad de vistas a un número entero expresado en millones.
    # Ejemplo: "1900 millones" → 1900000000.

def convertir_duracion_numerico(duracion: str) -> int:
    pass
    # Convierte la duración del video a un número entero expresado en segundos.
    # Ejemplo: "3:37" → 217 segundos.

def obtener_codigo(url: str) -> str:
    pass
    # Recibe una URL de YouTube.
    # Extrae y retorna el código único del video.
    # Ejemplo: "https://www.youtube.com/watch?v=bo_efYhYU2A" → "bo_efYhYU2A".

def formatear_fecha(fecha: str) -> date:
    pass
    # Recibe una fecha en formato YYYY-MM-DD.