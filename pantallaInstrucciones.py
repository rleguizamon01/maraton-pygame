import pygame
from ImagenConTexto import *
from Texto import *
from imagenes import amenaza4_0corazon, imgFlechas, imgTeclaD
from Boton import botonvolver

# ImagenConTexto (imagen, x, y, texto, tamletra, width, height)
flechas = ImagenConTexto(imgFlechas, 140, 120, "FLECHAS", 18, 140, 100)
teclaD = ImagenConTexto(imgTeclaD, 162, 285, "TECLA D", 18, 90, 90)
amenazaDerrotada = ImagenConTexto(amenaza4_0corazon, 155, 450, "", 0, 100, 100)

# Texto (x, y, texto, tamletra)
# -- MenuInstrucciones
textoFlechas = Texto(320, 165, "Move a Supertablet con las flechas del teclado", 24)
textoTeclaD = Texto(320, 320, "Combati a las Amenazas apretando la tecla D", 24)
textoAmenazaDerrotada = Texto(320, 485, "Una vez derrotadas, arrastralas hasta la Zona Segura", 22)


def dibujarPantallaInstrucciones():
    dibujarTitulo("INSTRUCCIONES")
    botonvolver.dibujarBoton("menuprincipal")

    dibujarrectangulofondo(140, 110)
    flechas.dibujarimagen()
    textoFlechas.dibujarTexto()

    dibujarrectangulofondo(140, 270)
    teclaD.dibujarimagen()
    textoTeclaD.dibujarTexto()

    dibujarrectangulofondo(140, 430)
    amenazaDerrotada.dibujarimagen()
    textoAmenazaDerrotada.dibujarTexto()