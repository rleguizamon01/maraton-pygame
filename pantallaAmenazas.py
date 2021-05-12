import pygame
from ImagenConTexto import *
from imagenes import *
from Texto import *
from RectanguloCursor import *
from Boton import botonvolver

# Imagen (imagen, x, y, nombreamenaza, tamletra, width, height)
amenaza1 = ImagenConTexto(amenazaimg1, 160, 150, "IMPOSTOR", 16, 100, 100)
amenaza2 = ImagenConTexto(amenazaimg2, 380, 150, "RANSOMWARE", 16, 100, 100)
amenaza3 = ImagenConTexto(amenazaimg3, 630, 150, "TROYANO", 16, 100, 100)
amenaza4 = ImagenConTexto(amenazaimg4, 880, 150, "VIRUS", 16, 100, 100)

textoPosicionarMouseAmenaza = Texto(130, 110, "Para conocer acerca de cada una apoya el mouse", 18, (153, 204, 255))
textoConsejosAmenaza = Texto(135, 370, "Para evitar cualquier tipo de MALWARE se recomienda usar un anti-malware", 21)
textoConsejosAmenaza2 = Texto(135, 400, "y mantenerlo actualizado.", 21)
textoConsejosAmenaza3 = Texto(135, 430, "Para evitar a los IMPOSTORES se recomienda solo aceptar en tus redes", 21)
textoConsejosAmenaza4 = Texto(135, 460, "sociales a gente que conozcas personalmente y NUNCA arreglar encuentros", 21)
textoConsejosAmenaza5 = Texto(135, 490, "con gente que no conozcas.", 21)

# Rectangulo cursor (tamletra, width, height, posarribaizquierda, posabajoderecha, imagen, text1, text2, text3, text4)
rectanguloamenaza1 = RectanguloCursor(14, 200, 300, amenaza1.getposarribaizquierda(), amenaza1.getposabajoderecha(),
                                      rectanguloazul, "Actua como una persona", "de tu edad en redes",
                                      "sociales, pero en", "realidad es un adulto.")
rectanguloamenaza2 = RectanguloCursor(15, 200, 300, amenaza2.getposarribaizquierda(), amenaza2.getposabajoderecha(),
                                      rectanguloazul, '"Secuestra" tus datos', "y luego pide un", "rescate.")
rectanguloamenaza3 = RectanguloCursor(15, 200, 300, amenaza3.getposarribaizquierda(), amenaza3.getposabajoderecha(),
                                      rectanguloazul, "Tiene el objetivo de", "robar tus datos.")
rectanguloamenaza4 = RectanguloCursor(15, 200, 300, amenaza4.getposarribaizquierda(), amenaza4.getposabajoderecha(),
                                      rectanguloazul, "Altera el", "funcionamiento de", "tu PC.")


def dibujarPantallaAmenazas():
    dibujarTitulo("AMENAZAS")
    textoPosicionarMouseAmenaza.dibujarTexto()
    dibujarrectangulofondo(180, 130)
    amenaza1.dibujarimagen()
    amenaza2.dibujarimagen()
    amenaza3.dibujarimagen()
    amenaza4.dibujarimagen()
    rectanguloamenaza1.dibujarrectangulo()
    rectanguloamenaza2.dibujarrectangulo()
    rectanguloamenaza3.dibujarrectangulo()
    rectanguloamenaza4.dibujarrectangulo()

    dibujarrectangulofondo(180, 350)

    botonvolver.dibujarBoton("menuprincipal")
    textoConsejosAmenaza.dibujarTexto()
    textoConsejosAmenaza2.dibujarTexto()
    textoConsejosAmenaza3.dibujarTexto()
    textoConsejosAmenaza4.dibujarTexto()
    textoConsejosAmenaza5.dibujarTexto()