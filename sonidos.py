import pygame

pygame.mixer.init()

# Sonidos
sonidoDisparo = pygame.mixer.Sound('sonidodisparo.wav')
sonidoClick = pygame.mixer.Sound('sonidoclick.wav')
sonidoImpacto = pygame.mixer.Sound('sonidoimpactoenemigo.wav')
sonidoVictoria = pygame.mixer.Sound('sonidovictoria.wav')

# Al iniciar el juego, el sonido comienza en ON
sonidoVolumen = True


def getSonidoVolumen():
    return sonidoVolumen


def setSonidoVolumen(valor):
    global sonidoVolumen
    sonidoVolumen = valor
