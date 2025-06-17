import pygame
from input import *

pygame.init()

ANCHO = 800
ALTO = 500

#CONFIGURACIONES
VENTANA = pygame.display.set_mode((ANCHO,ALTO)) 
icono = pygame.image.load("Programacion/Clases Anotaciones/utn_icono.jpg")
pygame.display.set_icon(icono)
pygame.display.set_caption("Primer juego en pygame")

# Creacion de Input
mi_input = crear_input(
                    ventana= VENTANA, 
                    fuente= ("consola", 20), 
                    color_activo="Red", 
                    color_inactivo= "Blue", 
                    posicion= (50,50), 
                    dimension= (200,35)
                    )


flag_run = True
while flag_run:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            flag_run = False
        elif evento.type == pygame.KEYDOWN:
            escribir(mi_input, evento)
                
    VENTANA.fill("Black")

    dibujar_input(mi_input)

    pygame.display.update()

pygame.quit()