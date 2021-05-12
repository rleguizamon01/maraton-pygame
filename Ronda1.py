# Version de python: 2.7.13
# Version de pygame: 1.9.2a0

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random
from eventos import *
from Boton import *
from imagenes import *
from Grilla import *
from sonidos import *
from musica import *
from configuracion import *
from Jugador import *
from Amenaza import *
from Zonaprotegida import *
from pantallas import *
from pantallaNivel1 import *
from ImagenConTexto import *
from Texto import *
from RectanguloCursor import *
from pantallaAmenazas import *
from pantallaInstrucciones import *
from pantallaVictoria import *
from pantallaMenuPrincipal import *
from pantallaElegirNivel import *
from pantallaNivel2 import *
from pantallaNivel3 import *
from GrillaScrolling import *
from ImagenConTextoCentrado import *
from Timer import *


# Inicializamos la libreria Pygame y demas variables
pygame.init()


def dibujarTodo():
    """ Dibuja todos los elementos necesarios para cada pantalla"""

    # Dibuja el fondo que es utilizado en todas las ventanas
    ventana.blit(bg, (0, 0))

    # Si la variable global es menuprincipal, dibuja los botones Jugar, Amenazas e Instrucciones
    if getPantallaActual() == "menuprincipal":
        dibujarMenuPrincipal()

    elif getPantallaActual() == "elegirnivel":
        dibujarPantallaElegirNivel()

    # Si la variable global es nivel1, comprueba si la amenaza esta en la Zona Segura, comprueba la posicion de las
    # amenazas, zona segura, supertablet y del proyectil y luego las dibuja. Tambien, dibuja el boton Volver
    elif getPantallaActual() == "nivel1":
        dibujarNivel1()

    elif getPantallaActual() == "nivel2":
        dibujarNivel2()

    elif getPantallaActual() == "reintentarnivel2":
        reintentarNivel2()

    # Si la varibale global es menuamenazas, dibuja un titulo, dos rectangulos con imagenes y texto cada uno y el boton
    # Volver
    elif getPantallaActual() == "menuamenazas":
        dibujarPantallaAmenazas()

    # Si la variableglobal es menuinstrucciones, dibuja un titulo, el boton Volver y tres rectangulos
    # con imagenes y texto cada uno
    elif getPantallaActual() == "menuinstrucciones":
        dibujarPantallaInstrucciones()

    # Si pantallaActual es victoria, dibuja un titulo, un texto que cambia segun la cantidad de pasos dados,
    # dos rectangulos y el boton Reintentar
    elif getPantallaActual() == "victorianivel1":
        dibujarPantallaVictoriaNivel1()

    elif getPantallaActual() == "victorianivel2":
        dibujarPantallaVictoriaNivel2()

    elif getPantallaActual() == "victorianivel3":
        dibujarPantallaVictoriaNivel3()

    elif getPantallaActual() == "reintentarnivel1":
        # Al presionar el boton Reintentar, los objetos vuelven a tomar sus parametros iniciales
        # Grilla
        reintentarNivel1()

    elif getPantallaActual() == "nivel3":
        dibujarNivel3()

    elif getPantallaActual() == "reintentarnivel3":
        print supertabletnivel3.getContadormA()
        # Al presionar el boton Reintentar, los objetos vuelven a tomar sus parametros iniciales
        # Grilla
        reintentarNivel3()

    # En todas las pantallas estan dibujados los botones Musica y Sonido
    botonmusica.dibujarBoton("musica")
    botonsonido.dibujarBoton("sonido")
    pygame.display.update()


while run():
    reloj = pygame.time.Clock()
    reloj.tick(20)
    getEventos()
    # Cada vez que se repita el bucle, se dibujan todos los elementos y las variables globales de eventos cambian su
    # valor a ""

    dibujarTodo()
    setEventos("")
pygame.quit()
