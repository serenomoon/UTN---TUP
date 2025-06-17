import pygame
from boton import *
import random

pygame.init()

ANCHO = 800
ALTO = 500

#CONFIGURACIONES
VENTANA = pygame.display.set_mode((ANCHO,ALTO)) 
icono = pygame.image.load("Programacion/Clases Anotaciones/utn_icono.jpg")
pygame.display.set_icon(icono)
pygame.display.set_caption("Primer juego en pygame")

#CREACION DE BOTONES

boton_gatito = crear_boton(
                            dimension = (100,100),
                            posicion= (50,50),
                            ventana= VENTANA,
                            imagen= "Programacion/Clases Anotaciones/gatito.jpeg",
                            color_borde= "Green"
                            )

boton_utn = crear_boton(
                        dimension = (100,100),
                        posicion= (250,350),
                        ventana= VENTANA,
                        imagen= "Programacion/Clases Anotaciones/utn_icono.jpg",
                        color_borde= "Pink"
                        )

boton_texto = crear_boton(
                            dimension = (100,200),
                            color_borde= "Pink",
                            ventana= VENTANA,
                            fuente= ("consolas", 20),
                            texto= ("Presioname"),
                            posicion= (50,250)
                        )

pygame.mixer.init() # Inicializa el mixer para poder reproducir un sonido
pygame.mixer.music.load("Programacion/Clases Anotaciones/OK.mp3") # Cargp el sonido

fuente_texto = pygame.font.SysFont("arial", 20) # Creo la fuente del texto y el tamaño

lista_botones = [boton_gatito, boton_utn, boton_texto] # Pongo los botones en una lista

flag_run = True
while flag_run:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            flag_run = False
        elif evento.type == pygame.MOUSEBUTTONDOWN: # hice click
            if boton_gatito["Rectangulo"].collidepoint(evento.pos): # Devuelve True si hago click dentro del rectangulo que le asigne al boton del gatito
                boton_gatito["Presionado"] = True
            elif boton_texto["Rectangulo"].collidepoint(evento.pos):
                 pygame.mixer.music.play()
                

    dibujar_boton(boton_gatito)
    if boton_gatito["Presionado"]:
            texto = fuente_texto.render("Miau", False, "Green", "Orange") # Creo la superficie de la fuente, color y fondo.
            x = random.randint(50,700)
            y = random.randint(50,400)
            VENTANA.blit(texto, (x,y)) # Paso texto y posicion
            boton_gatito["Presionado"] = False # Dejo de presionar el boton

    dibujar_lista_botones(lista_botones)


    pygame.display.update()

pygame.quit()