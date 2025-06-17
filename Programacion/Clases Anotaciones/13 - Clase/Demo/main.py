import pygame

pygame.init()

ANCHO = 800
ALTO = 500
ROJO = (150,25,33) # Definimos los colores para que quede mas ordenado

#CONFIGURACIONES
VENTANA = pygame.display.set_mode((ANCHO,ALTO)) # Ancho y alto de la ventana
# VENTANA.fill("Green") # Predefinido
VENTANA.fill(ROJO) # RGB
icono = pygame.image.load("Programacion/Clases Anotaciones/utn_icono.jpg") # Cargamos la imagen en una variable
pygame.display.set_icon(icono) # La ponemos como icono de la ventana ("Seteamos")
pygame.display.set_caption("Primer juego en pygame") # Le cambiamos el titulo a la ventana

gatito = pygame.image.load("Programacion/Clases Anotaciones/gatito.jpeg") # Cargamos imagen gatito

VENTANA.blit(gatito,(50,50)) # Pegamos sobre la ventana una imagen y le ponemos sus coordenadas
# (0,0) es la esquima superior izquierda
# (800,500) La esquina inferior derecha en este caso ("Blitear")

x, y = gatito.get_rect().topleft # Asociamos la imagen a una superficie (un rectangulo)


flag_run = True
while flag_run:
    for evento in pygame.event.get(): # Devuelve una lista de los eventos capturados

        # if evento.type == pygame.MOUSEMOTION: # Chequeo si el mouse se esta moviendo x ej

        if evento.type == pygame.QUIT: # Ya puedo mover la ventana y cerrarla desde la X
            flag_run = False

    VENTANA.fill(ROJO) # Para que no quede un borron atras de la imagen del gatito (refrescamos fondo)
    VENTANA.blit(gatito,(10 + x,10 + y)) # Movemos el gatito
    x += .02 # Movemos la imagen sumandole al valor x e y en este caso
    y += .02
    pygame.display.update()

pygame.quit()