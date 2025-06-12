from lady_gaga import playlist_lady_gaga
from funciones_generales import *

# def mostrar_colaboradores(tema: str) -> None:
#     colaboradores = obtener_colaboradores(tema)
#     if len(colaboradores) > 1:
#         print("Colaboradores:", end=" ")
#         for colaborador in colaboradores:
#             print(f"{colaborador} -", end=" ")
#         print("")

# def mostrar_playlist(playlist: dict) -> None:
#     print(f"Titulo: {obtener_nombre_tema(playlist["Tema"])}")
#     mostrar_colaboradores(playlist["Tema"])
#     print(f"Vistas: {convertir_vistas_numerico(playlist["Vistas"])} seg")
#     print(f"Link: {playlist["Link Youtube"]}")
#     print(f"Fecha de lanzamiento (date): {formatear_fecha(playlist["Fecha lanzamiento"])}")
#     print("")



# def mostrar_datos(playlist: list) -> None:
#     for temas in playlist:
#         mostrar_playlist(temas)

def normalizar_datos(playlist: list) -> list:
        playlist_normalizada = []
        for video in playlist:
            titulo = obtener_nombre_tema(video["Tema"])
            colaboradores = obtener_colaboradores(video["Tema"])
            vistas = convertir_vistas_numerico(video["Vistas"])
            duracion = convertir_duracion_numerico(video["Duracion"])
            link = video["Link Youtube"]
            fecha = formatear_fecha(video["Fecha lanzamiento"])

            video_normalizado = {
                "Título": titulo,
                "Colaboradores": colaboradores,
                "Vistas": vistas,
                "Duración": duracion,
                "Link": link,
                "Fecha de lanzamiento": fecha
            }

            playlist_normalizada.append(video_normalizado)
        return playlist_normalizada

def mostrar_temas(playlist: list) -> None:
    print(f"{'Título':<45} {'Duración'}")
    for video in playlist:
        duracion = video["Duración"]
        minutos = duracion // 60
        segundos = duracion % 60
        print(f"{video['Título']:<45} {minutos}:{segundos:02d}")


def ordenar_por_duracion(playlist: list) -> list:
    for i in range(len(playlist)-1):
        for j in range(len(playlist)-1-i):
            duracion_actual = playlist[j]["Duración"]
            duracion_siguiente = playlist[j+1]["Duración"]
            
            if duracion_siguiente > duracion_actual:
                aux = playlist[j]
                playlist[j] = playlist[j+1]
                playlist[j+1] = aux

def promedio_vistas_millones(playlist: list) -> int:
    total_vistas = 0
    for video in playlist:
        total_vistas += video["Vistas"]
    
    promedio = total_vistas / len(playlist)
    return promedio / 1_000_000
   

def videos_max_min(playlist: list, modo: str ="max") -> list:

    valor_extremo = playlist[0]["Vistas"]
    
    for video in playlist:
        if modo == "max":
            if video["Vistas"] > valor_extremo:
                valor_extremo = video["Vistas"]
        else:
            if video["Vistas"] < valor_extremo:
                valor_extremo = video["Vistas"]
    
    resultados = []
    for video in playlist:
        if video["Vistas"] == valor_extremo:
            resultados.append(video)
    
    return resultados


def buscar_video_por_codigo(playlist: list, codigo_buscado: str) -> str:
    video_encontrado = None
    for video in playlist:
        codigo = obtener_codigo(video["Link"])
        if codigo == codigo_buscado:
            video_encontrado = video
    return video_encontrado


def listar_videos_por_colaborador(playlist: list, colaborador_buscado: str) -> list:
    resultados = []
    colaborador_buscado = colaborador_buscado.lower()

    for video in playlist:
        colaboradores = []
        colaborador = None 
        for colaborador in video["Colaboradores"]:
            colaboradores.append(colaborador.lower())

        if colaborador_buscado in colaboradores:
            resultados.append(video)

    return resultados


def listar_videos_por_mes(playlist: list, mes_buscado: int) -> list:
    resultados = []
    
    for video in playlist:
        mes_video = video["Fecha de lanzamiento"].month
        if mes_video == mes_buscado:
            resultados.append(video)
    
    return resultados
