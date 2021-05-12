import pygame
from Boton import *

anchoventana, altoventana = pygame.display.get_surface().get_size()
filastotal = 1
columnastotal = 3
xmargen = 100
ymargen = 270
anchoboton = (anchoventana - xmargen * (columnastotal + 1)) / columnastotal
altoboton = (altoventana - ymargen * (filastotal + 1)) / filastotal


def xyBotonMenuNivel(filanivel, columnanivel):
    global xmargen, ymargen, anchoboton, altoboton

    xboton = xmargen * columnanivel + anchoboton * (columnanivel - 1)
    yboton = ymargen * filanivel + altoboton * (filanivel - 1)

    return xboton, yboton


# Botones (permitir eventos, tamano de letra, x, y, width, height, texto, colores, colores secundarios (opcional),
# texto secundario ( opcional))
botonnivel1 = Boton(True, 40, xyBotonMenuNivel(1, 1)[0], xyBotonMenuNivel(1, 1)[1], anchoboton, altoboton, "1", coloresazules)
botonnivel2 = Boton(False, 40, xyBotonMenuNivel(1, 2)[0], xyBotonMenuNivel(1, 2)[1], anchoboton, altoboton, "2", coloresgrises)
botonnivel3 = Boton(False, 40, xyBotonMenuNivel(1, 3)[0], xyBotonMenuNivel(1, 3)[1], anchoboton, altoboton, "3", coloresgrises)

def dibujarPantallaElegirNivel():
    botonnivel1.dibujarBoton("nivel1")
    botonnivel2.dibujarBoton("nivel2")
    botonnivel3.dibujarBoton("nivel3")

    botonvolver.dibujarBoton("menuprincipal")


