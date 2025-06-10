from datetime import datetime
from lady_gaga import playlist_lady_gaga

def split_string(cadena: str, caracter: str = " ", numero: int = 2) -> list:
    """Separa un array en dos partes y devuelve una de las dos o ambos

    Args:
        cadena (str): string a dividir
        caracter (str, optional): Caracter donde se efectua la division. Defaults to " ".
        numero (int, optional): Parte del string que se devuelve. Defaults to 2.

    Returns:
        list: _description_
    """
    spliteado = cadena.split(caracter)
    if numero == 0:
        spliteado = spliteado[0]
    elif numero == 1:
        spliteado = spliteado[1]
    return spliteado


def obtener_colaboradores(titulo: str) -> list:
    """Recibe string de tema y colaboradores, devuelve colaboradores en un array

    Args:
        titulo (str): Nombre del tema y sus colaboradores

    Returns:
        list: Lista de colaboradores
    """
    colaboradores_recortados = split_string(titulo,"-",0)
    nueva_lista = []
    for i in range(len(colaboradores_recortados.split("|"))):
        nuevo = colaboradores_recortados.split("|")[i].strip()
        nueva_lista.append(nuevo)
    return nueva_lista


def obtener_nombre_tema(titulo: str) -> str:
    """Recibe el título del tema y colaboradores.
    Retorna solo el nombre del tema

    Args:
        titulo (str): tema y colaboradores

    Returns:
        str: nombre del tema
    """
    tema = titulo
    for i in range(len(titulo)):
        if titulo[i] == "-":
            tema = split_string(titulo,"-",1).strip()

    return tema


def convertir_vistas_numerico(vistas: str) -> int:
    """Convierte un numero en numeros y letras a solo numeros.
    Ejemplo: "1900 millones" → 1900000000.

    Args:
        vistas (str): numero y letras

    Returns:
        int: numero entero
    """
    numero_dividido = split_string(vistas)
    
    if numero_dividido[1] == "millones":
        numero = int(numero_dividido[0])*1_000_000
    elif numero_dividido[0] == "mil":
        numero = int(numero_dividido[0])*1_000
    return numero


def convertir_duracion_numerico(duracion: str) -> int:
    """Convierte formato min y seg a un número entero expresado en segundos.
        Ejemplo: "3:37" → 217 segundos

    Args:
        duracion (str): minutos y segundo ingresados

    Returns:
        int: segundos
    """
    segundos_divididos = split_string(duracion,":")
    segundos = int(segundos_divididos[0])*60 + int(segundos_divididos[1])
    return segundos


def obtener_codigo(url: str) -> str:
    """Recibe una URL de YouTube.
        Extrae y retorna el código único del video.
        Ejemplo: "https://www.youtube.com/watch?v=bo_efYhYU2A" → "bo_efYhYU2A".

    Args:
        url (str): link del video

    Returns:
        str: Codigo del video
    """
    codigo = split_string(url,"?v=",1)
    return codigo


def formatear_fecha(fecha: str) -> datetime:
    """Recibe una fecha en formato YYYY-MM-DD.
    Retorna la fecha como un objeto de tipo date.

    Args:
        fecha (str): fecha string

    Returns:
        datetime: fecha tipo date
    """
    fecha_convertida = datetime.strptime(fecha, "%Y-%m-%d").date()
    return fecha_convertida