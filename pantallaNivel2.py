import pygame
from Jugador import *
from Zonaprotegida import *
from Boton import *
from Grilla import *
from Amenaza import *
from Texto import *
from ImagenConTextoCentrado import *
from Timer import *
from configuracion import *
from imagenes import *


nivel2 = Grilla(8, 5)

# Jugador (xinicial, yinicial)
supertabletnivel2 = Jugador(3, 2)

# Amenaza (xinicial, yinicial)
amenaza1nivel2 = Amenaza(3, 3)
amenaza2nivel2 = Amenaza(4, 3)
amenaza3nivel2 = Amenaza(5, 3)
amenaza4nivel2 = Amenaza(6, 3)
amenaza5nivel2 = Amenaza(5, 4)

# ZonaProtegida (xinicial, yinicial)
zonaprotegida1nivel2 = Zonaprotegida(2, 2)
zonaprotegida2nivel2 = Zonaprotegida(2, 4)
zonaprotegida3nivel2 = Zonaprotegida(4, 4)
zonaprotegida4nivel2 = Zonaprotegida(7, 2)
zonaprotegida5nivel2 = Zonaprotegida(7, 4)

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
cron2 = Time(True, "Arial", 30, 90, 400)


def dibujarNivel2():

    amenaza1nivel2.setCantCorazones(0)
    amenaza2nivel2.setCantCorazones(0)
    amenaza3nivel2.setCantCorazones(0)
    amenaza4nivel2.setCantCorazones(0)
    amenaza5nivel2.setCantCorazones(0)

    xyamenaza1 = amenaza1nivel2.getxycorazonesamenaza()
    xyamenaza2 = amenaza2nivel2.getxycorazonesamenaza()
    xyamenaza3 = amenaza3nivel2.getxycorazonesamenaza()
    xyamenaza4 = amenaza4nivel2.getxycorazonesamenaza()
    xyamenaza5 = amenaza5nivel2.getxycorazonesamenaza()

    xyzonaprotegida1 = zonaprotegida1nivel2.getXYZonaProtegida()
    xyzonaprotegida2 = zonaprotegida2nivel2.getXYZonaProtegida()
    xyzonaprotegida3 = zonaprotegida3nivel2.getXYZonaProtegida()
    xyzonaprotegida4 = zonaprotegida4nivel2.getXYZonaProtegida()
    xyzonaprotegida5 = zonaprotegida5nivel2.getXYZonaProtegida()


    listaxyzonasprotegidas = getXyZonasProtegidas(xyzonaprotegida1, xyzonaprotegida2, xyzonaprotegida3, xyzonaprotegida4, xyzonaprotegida5)
    listaxyamenazas = getXyAmenazas(xyamenaza1, xyamenaza2, xyamenaza3, xyamenaza4, xyamenaza5)

    supertabletnivel2.moverProyectil(nivel2.getGrilla(), listaxyamenazas)
    xyproyectil = supertabletnivel2.getXyProyectil()

    amenaza1nivel2.moverAmenaza(supertabletnivel2.getXyJugador(), xyproyectil)
    amenaza2nivel2.moverAmenaza(supertabletnivel2.getXyJugador(), xyproyectil)
    amenaza3nivel2.moverAmenaza(supertabletnivel2.getXyJugador(), xyproyectil)
    amenaza4nivel2.moverAmenaza(supertabletnivel2.getXyJugador(), xyproyectil)
    amenaza5nivel2.moverAmenaza(supertabletnivel2.getXyJugador(), xyproyectil)

    zonaprotegida1nivel2.comprobarAmenaza(listaxyamenazas)
    zonaprotegida2nivel2.comprobarAmenaza(listaxyamenazas)
    zonaprotegida3nivel2.comprobarAmenaza(listaxyamenazas)
    zonaprotegida4nivel2.comprobarAmenaza(listaxyamenazas)
    zonaprotegida5nivel2.comprobarAmenaza(listaxyamenazas)

    comprobarAmenazaZonaSegura(listaxyzonasprotegidas, "nivel2")

    supertabletnivel2.moverJugador(nivel2.getGrilla(), listaxyamenazas)
    xyjugador = supertabletnivel2.getXyJugador()

    nivel2.dibujarZonaDeTransporte(xyjugador, listaxyamenazas, xyproyectil, listaxyzonasprotegidas)

    comprobarRehacerAmenaza()

    dibujarrectangulofondo(60, 7, 1000, 71)
    textoContadorPasos1 = Texto(100, 23, "Contador de pasos:" + supertabletnivel2.getContadorPasos(60)[0], 30)
    textoContadorPasos1.dibujarTexto()

    textoContadormA = Texto(600, 23, "Contador de mA: " + str(supertabletnivel2.getContadormA()), 30)
    textoContadormA.dibujarTexto()

    botonvolver.dibujarBoton("elegirnivel")

    if supertabletnivel2.getContadormA() <= 0:
        setPantallaActual("reintentarnivel2")
    botonreintentar.dibujarBoton("reintentarnivel2")

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
    cron2.dibujarTiempo()



def comprobarRehacerAmenaza():
    amenaza1nivel2.comprobarRehacer(supertabletnivel2.getMovioAmenaza()[0], supertabletnivel2.getMovioAmenaza()[1],
                                supertabletnivel2.getMovioAmenaza()[2])
    amenaza2nivel2.comprobarRehacer(supertabletnivel2.getMovioAmenaza()[0], supertabletnivel2.getMovioAmenaza()[1],
                                    supertabletnivel2.getMovioAmenaza()[2])
    amenaza3nivel2.comprobarRehacer(supertabletnivel2.getMovioAmenaza()[0], supertabletnivel2.getMovioAmenaza()[1],
                                    supertabletnivel2.getMovioAmenaza()[2])
    amenaza4nivel2.comprobarRehacer(supertabletnivel2.getMovioAmenaza()[0], supertabletnivel2.getMovioAmenaza()[1],
                                    supertabletnivel2.getMovioAmenaza()[2])
    amenaza5nivel2.comprobarRehacer(supertabletnivel2.getMovioAmenaza()[0], supertabletnivel2.getMovioAmenaza()[1],
                                    supertabletnivel2.getMovioAmenaza()[2])

def reintentarNivel2():
    nivel2.__init__(8, 5)

    # Jugador (xinicial, yinicial)
    supertabletnivel2.__init__(3, 2)

    # Amenaza (xinicial, yinicial)
    amenaza1nivel2.__init__(3, 3)
    amenaza2nivel2.__init__(4, 3)
    amenaza3nivel2.__init__(5, 3)
    amenaza4nivel2.__init__(6, 3)
    amenaza5nivel2.__init__(5, 4)

    # ZonaProtegida (xinicial, yinicial)
    zonaprotegida1nivel2.__init__(2, 2)
    zonaprotegida2nivel2 .__init__(2, 4)
    zonaprotegida3nivel2.__init__(4, 4)
    zonaprotegida4nivel2.__init__(7, 2)
    zonaprotegida5nivel2.__init__(7, 4)

    # Cronometro reinicio
    cron2.__init__(True, "Arial", 30, 90, 400)

    setPantallaActual("nivel2")
