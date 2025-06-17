import pygame

def crear_boton(dimension, posicion, ventana, color_borde, imagen = None, fuente = None, texto = None):
    boton = {}
    boton["Ventana"] = ventana
    boton["Dimension"] = dimension # Tupla(Ancho y Alto)
    boton["Posicion"] = posicion # Tupla(X,Y)
    boton["ColorBorde"] = color_borde
    boton["Presionado"] = False # Para ver si esta o no presionado

    if imagen != None:
        img = pygame.image.load(imagen) # Cargo la imagen
        boton["Superficie"] = pygame.transform.scale(img, boton["Dimension"]) # La redimensiono
    else:
        tipo, tamaño = fuente
        text_fuente = pygame.font.SysFont(tipo, tamaño, True) # True es si es negrita o no
        boton["Superficie"] = text_fuente.render(texto, False, "Blue", "White")

    boton["Rectangulo"] = boton["Superficie"].get_rect() # Tomo la superficie del boton para hacerle una base y posicionarlo
    boton["Rectangulo"].topleft = boton["Posicion"] # Lo posiciono tomando como parametro la esquina superior izquierda

    return boton


def dibujar_boton(boton: dict):
    boton["Ventana"].blit(boton["Superficie"], boton["Posicion"]) # Colocamos el boton
    pygame.draw.rect(boton["Ventana"], boton["ColorBorde"], boton["Rectangulo"], 2) # Le ponemos el borde, 2 seria el ancho del borde


def dibujar_lista_botones(lista_botones):
    for boton in lista_botones:
         dibujar_boton(boton) # Llamo a los botones