import pygame

def crear_input(ventana, fuente, color_activo, color_inactivo, posicion, dimension):
    input_text = {}
    input_text["Ventana"] = ventana
    input_text["ColorActivo"] = color_activo
    input_text["ColorInactivo"] = color_inactivo
    input_text["Posicion"] = posicion
    input_text["Dimension"] = dimension
    tipo, tamaño = fuente
    input_text["Fuente"] = pygame.font.SysFont(tipo, tamaño)
    x, y = input_text["Posicion"]
    w, h = input_text["Dimension"]
    input_text["Rectangulo"] = pygame.Rect(x, y , w, h)
    input_text["Texto"] = ""

    input_text["Activo"] = False
    input_text["ColorActual"] = input_text["ColorInactivo"]

    return input_text


def dibujar_input(input_text: dict):
    texto = input_text["Fuente"].render(input_text["Texto"], True, input_text["ColorActual"]) # Renderizo texto, el True es antialiasing (para q se vea mejor)
    x, y = input_text["Posicion"]
    # x, y = input_text["Rectangulo"].topleft # Puedo hacerlo de esta forma tambien
    # x = input_text["Rectangulo"].x # o individualmente
    # y = input_text["Rectangulo"].y # o individualmente
    input_text["Ventana"].blit(texto, (x+5,y+10)) # Para que no empieze tan en la punta del inputbox
    pygame.draw.rect(input_text["Ventana"], input_text["ColorActual"], input_text["Rectangulo"], 1, 3) # 1 es ancho del brode, 3 para redondear 


def escribir(input_text: dict, evento):
    if evento.key == pygame.K_ESCAPE:
        input_text["Texto"] = ""
    elif evento.key == pygame.K_BACKSPACE:
        input_text["Texto"] = input_text["Texto"][:-1]
    else:
        input_text["Texto"] += evento.unicode