import pygame
from configuracion import cantPixelesPorLadoCasilla, cantidadDeCasillasPorLado
from random import choice

# Cargamos las imagenes
imgSuperTablet = pygame.image.load("supertablet.png")
imgSuperTabletVictoria = pygame.image.load("supertabletvictoria.png")
imgPared = pygame.image.load("pared.png")
listaAmenazas = ["amenaza1.png", "amenaza2.png", "amenaza3.png", "amenaza4.png"]
imgAreaProtegida = pygame.image.load("areaprotegida.png")
imgDisparo = pygame.image.load("disparo.png")
imgPiso = pygame.image.load("piso.png")
imgFlechas = pygame.image.load("flechas.png")
imgTeclaD = pygame.image.load("teclad.png")
cuadro = pygame.image.load("cuadro.png")
bg = pygame.image.load('fondo.png')

# Escalar imagenes
imgSuperTablet = pygame.transform.scale(imgSuperTablet, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
imgSuperTabletVictoria = pygame.transform.scale(imgSuperTabletVictoria,
                                                (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
imgPared = pygame.transform.scale(imgPared, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
# imgAmenaza = pygame.transform.scale(imgAmenaza, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
imgAreaProtegida = pygame.transform.scale(imgAreaProtegida, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
imgDisparo = pygame.transform.scale(imgDisparo, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
imgPiso = pygame.transform.scale(imgPiso, (
    cantPixelesPorLadoCasilla * cantidadDeCasillasPorLado, cantPixelesPorLadoCasilla * cantidadDeCasillasPorLado))
bg = pygame.transform.scale(bg, (1152, 648))

amenaza4_3corazon = pygame.image.load("amenaza43.png")
amenaza4_2corazon = pygame.image.load("amenaza42.png")
amenaza4_1corazon = pygame.image.load("amenaza41.png")
amenaza4_0corazon = pygame.image.load("amenaza40.png")

amenaza4_3corazon = pygame.transform.scale(amenaza4_3corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
amenaza4_2corazon = pygame.transform.scale(amenaza4_2corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
amenaza4_1corazon = pygame.transform.scale(amenaza4_1corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
amenaza4_0corazon = pygame.transform.scale(amenaza4_0corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))

amenaza3_3corazon = pygame.image.load("amenaza33.png")
amenaza3_2corazon = pygame.image.load("amenaza32.png")
amenaza3_1corazon = pygame.image.load("amenaza31.png")
amenaza3_0corazon = pygame.image.load("amenaza30.png")

amenaza3_3corazon = pygame.transform.scale(amenaza3_3corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
amenaza3_2corazon = pygame.transform.scale(amenaza3_2corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
amenaza3_1corazon = pygame.transform.scale(amenaza3_1corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
amenaza3_0corazon = pygame.transform.scale(amenaza3_0corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))

amenaza2_3corazon = pygame.image.load("amenaza23.png")
amenaza2_2corazon = pygame.image.load("amenaza22.png")
amenaza2_1corazon = pygame.image.load("amenaza21.png")
amenaza2_0corazon = pygame.image.load("amenaza20.png")

amenaza2_3corazon = pygame.transform.scale(amenaza2_3corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
amenaza2_2corazon = pygame.transform.scale(amenaza2_2corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
amenaza2_1corazon = pygame.transform.scale(amenaza2_1corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
amenaza2_0corazon = pygame.transform.scale(amenaza2_0corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))

amenaza1_3corazon = pygame.image.load("amenaza13.png")
amenaza1_2corazon = pygame.image.load("amenaza12.png")
amenaza1_1corazon = pygame.image.load("amenaza11.png")
amenaza1_0corazon = pygame.image.load("amenaza10.png")

amenaza1_3corazon = pygame.transform.scale(amenaza1_3corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
amenaza1_2corazon = pygame.transform.scale(amenaza1_2corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
amenaza1_1corazon = pygame.transform.scale(amenaza1_1corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))
amenaza1_0corazon = pygame.transform.scale(amenaza1_0corazon, (cantPixelesPorLadoCasilla, cantPixelesPorLadoCasilla))

rectanguloazul = pygame.image.load('RectanguloCursor.png')
rectangulogris = pygame.image.load('rectangulocursorgris.png')

amenazaimg1 = pygame.image.load('amenaza1.png')
amenazaimg2 = pygame.image.load('amenaza2.png')
amenazaimg3 = pygame.image.load('amenaza3.png')
amenazaimg4 = pygame.image.load('amenaza4.png')

listaAmenazas = [[amenaza4_3corazon, amenaza4_2corazon, amenaza4_1corazon, amenaza4_0corazon],
                 [amenaza3_3corazon, amenaza3_2corazon, amenaza3_1corazon, amenaza3_0corazon],
                 [amenaza2_3corazon, amenaza2_2corazon, amenaza2_1corazon, amenaza2_0corazon],
                 [amenaza1_3corazon, amenaza1_2corazon, amenaza1_1corazon, amenaza1_0corazon]]
listaAmenazas4 = choice(listaAmenazas)
