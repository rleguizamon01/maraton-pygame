import pygame
from Jugador import *
from Zonaprotegida import *
from Boton import *
from Grilla import *
from Amenaza import *
from Texto import *
from ImagenConTexto import *
from imagenes import *
from ImagenConTextoCentrado import *
from Timer import *
from configuracion import *

nivel1 = Grilla(8, 8)

# Jugador (xinicial, yinicial)
supertablet = Jugador(2, 2)

# Amenaza (xinicial, yinicial)
amenazanivel1 = Amenaza(6, 3)

# ZonaProtegida (xinicial, yinicial)
zonaprotegida1 = Zonaprotegida(4, 4)

# Cuadro de Bateria
titulo       = ImagenConTextoCentrado(cuadro, 90, 100, "Gasto de Bateria", 16, 155, 50)
mov          = ImagenConTextoCentrado(cuadro, 90, 160, "Caminar", 16, 90, 25)
movnum       = ImagenConTextoCentrado(cuadro, 220, 160, "10", 16, 25, 25)
disparar     = ImagenConTextoCentrado(cuadro, 90, 185, "Disparar", 16, 90, 25)
disnum       = ImagenConTextoCentrado(cuadro, 220, 185, "10", 16, 25, 25)
empujar      = ImagenConTextoCentrado(cuadro, 90, 210, "Empujar", 16, 90, 25)
empnum       = ImagenConTextoCentrado(cuadro, 220, 210, "15", 16, 25, 25)
empujar2     = ImagenConTextoCentrado(cuadro, 90, 235, "Empujar 2", 16, 90, 25)
emp2num      = ImagenConTextoCentrado(cuadro, 220, 235, "200", 16, 25, 25)

#Cronometro
cron = Time(True, "Arial", 30, 90, 400)

def dibujarNivel1():
    xyamenaza1 = amenazanivel1.getxycorazonesamenaza()
    listaxyamenazas = getXyAmenazas(xyamenaza1)

    supertablet.moverProyectil(nivel1.getGrilla(), listaxyamenazas)
    xyproyectil = supertablet.getXyProyectil()

    amenazanivel1.moverAmenaza(supertablet.getXyJugador(), xyproyectil)

    supertablet.moverJugador(nivel1.getGrilla(), listaxyamenazas)
    xyjugador = supertablet.getXyJugador()

    zonaprotegida1.comprobarAmenaza(listaxyamenazas)
    xyzonaprotegida1 = zonaprotegida1.getXYZonaProtegida()
    xyzonasprotegidas = getXyZonasProtegidas(xyzonaprotegida1)

    nivel1.dibujarZonaDeTransporte(xyjugador, listaxyamenazas, xyproyectil, xyzonasprotegidas)

    comprobarAmenazaZonaSegura(xyzonasprotegidas, "nivel1")
    comprobarRehacerAmenaza()


    dibujarrectangulofondo(60, 7, 1000, 71)
    textoContadorPasos1 = Texto(100, 23, "Contador de pasos:" + supertablet.getContadorPasos(15)[0], 30)
    textoContadorPasos1.dibujarTexto()

    textoContadormA = Texto(600, 23, "Contador de mA: " + str(supertablet.getContadormA()), 30)
    textoContadormA.dibujarTexto()

    botonvolver.dibujarBoton("elegirnivel")

    if supertablet.getContadormA() <= 0:
        setPantallaActual("reintentarnivel1")
    botonreintentar.dibujarBoton("reintentarnivel1")

    titulo.dibujarimagenn()
    mov.dibujarimagenn()
    movnum.dibujarimagenn()
    disparar.dibujarimagenn()
    disnum.dibujarimagenn()
    empujar.dibujarimagenn()
    empnum.dibujarimagenn()
    empujar2.dibujarimagenn()
    emp2num.dibujarimagenn()
    
    # Cronometro
    cron.dibujarTiempo()

def comprobarRehacerAmenaza():
    amenazanivel1.comprobarRehacer(supertablet.getMovioAmenaza()[0], supertablet.getMovioAmenaza()[1], supertablet.getMovioAmenaza()[2])

def reintentarNivel1():
    nivel1.__init__(8, 8)

    # Jugador (xinicial, yinicial)
    supertablet.__init__(2, 2)

    # Amenaza (xinicial, yinicial)

    # ZonaProtegida (xinicial, yinicial)
    amenazanivel1.__init__(6, 3)
    zonaprotegida1.__init__(4, 4)
    
    # Cronometro reinicio
    cron.__init__(True, "Arial", 30, 90, 400)
    setPantallaActual("nivel1")
