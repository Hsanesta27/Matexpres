import pygame
from Scripts.Pantallas import *
from Scripts.Preguntas import *

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Raquel ponnos un 10 ;)")

icono = pygame.image.load("../Recursos/Imagen/icono.png")
pygame.display.set_icon(icono)

Música=pygame.mixer.music.load("../Recursos/Sonidos/Mii_theme.mp3")

'''

Lista de variables:
0 = QUIT event
1 = MOUSEBUTTONUP
2 = MOUSEBUTTONDOWN
3 = KEYUP
4 = KEYDOWN
5 = MOUSEMOTION

'''

Eventos = [True, False, False, (), (), ()]
pygame.mixer.music.play(-1)
Pantalla.CargaInicio()

while Eventos[0]:

    pygame.display.update()
    screen.fill((255, 227, 176))

    if Pantalla.Pantalla == 0 and Pantalla.Cargado == 0:
        Pantalla.Inicio()
    elif Pantalla.Pantalla == 0:
        Pantalla.CargaInicio()

    if Pantalla.Pantalla == 1 and Pantalla.Cargado == 1:
        Pantalla.Pantalla1()
    elif Pantalla.Pantalla == 1:
        Pantalla.CargaPantalla1()

    if Pantalla.Pantalla==2 and Pantalla.Cargado==2:
        Pantalla.Pantalla2()
    elif Pantalla.Pantalla==2:
        Pantalla.CargaPantalla2()

    if Pantalla.Pantalla == 3 and Pantalla.Cargado == 3:
        Pantalla.Pantalla3()
    elif Pantalla.Pantalla == 3:
        Pantalla.CargaPantalla3()

    if Pantalla.Pantalla == 4 and Pantalla.Cargado == 4:
        Pantalla.Pantalla4()
    elif Pantalla.Pantalla == 4:
        Pantalla.CargaPantalla4()

    if Pantalla.Pantalla == 5 and Pantalla.Cargado == 5:
        Pantalla.Pantalla5()
    elif Pantalla.Pantalla == 5:
        Pantalla.CargaPantalla5()

    if Pantalla.Pantalla == 6 and Pantalla.Cargado == 6:
        Pantalla.Pantalla6()
    elif Pantalla.Pantalla == 6:
        Pantalla.CargaPantalla6()

    if Pantalla.Pantalla == 7 and Pantalla.Cargado == 7:
        Pantalla.Pantalla7()
    elif Pantalla.Pantalla == 7:
        Pantalla.CargaPantalla7()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            Eventos[0] = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Eventos[2] = True
                Eventos[1] = False

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                Eventos[1] = True
                Eventos[2] = False
        if event.type == pygame.MOUSEMOTION:
            Eventos[5] = event.pos