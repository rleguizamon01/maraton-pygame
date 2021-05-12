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

nivel3 = Grilla(10, 10)

# Jugador (xinicial, yinicial)
supertabletnivel3 = Jugador(3, 2)

# Amenaza (xinicial, yinicial)
amenaza1nivel3 = Amenaza(3, 3)
amenaza2nivel3 = Amenaza(4, 5)
amenaza3nivel3 = Amenaza(5, 3)
amenaza4nivel3 = Amenaza(6, 6)


# ZonaProtegida (xinicial, yinicial)
zonaprotegida1nivel3 = Zonaprotegida(2, 4)
zonaprotegida2nivel3 = Zonaprotegida(2, 6)
zonaprotegida3nivel3 = Zonaprotegida(4, 7)
zonaprotegida4nivel3 = Zonaprotegida(7, 2)

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
cron3 = Time(True, "Arial", 30, 90, 400)

def dibujarNivel3():
    # Setea paredes en posiciones especificas de la grilla (x, y)
    nivel3.setParedes(2, 2)
    nivel3.setParedes(9, 9)
    nivel3.setParedes(2, 9)
    nivel3.setParedes(9, 2)

    amenaza2nivel3.setDireccionMovimiento("HORIZONTAL")
    amenaza3nivel3.setDireccionMovimiento("HORIZONTAL")

    nivel3.setPixelesLadoCasilla(60)

    xyamenaza1 = amenaza1nivel3.getxycorazonesamenaza()
    xyamenaza2 = amenaza2nivel3.getxycorazonesamenaza()
    xyamenaza3 = amenaza3nivel3.getxycorazonesamenaza()
    xyamenaza4 = amenaza4nivel3.getxycorazonesamenaza()

    xyzonaprotegida1 = zonaprotegida1nivel3.getXYZonaProtegida()
    xyzonaprotegida2 = zonaprotegida2nivel3.getXYZonaProtegida()
    xyzonaprotegida3 = zonaprotegida3nivel3.getXYZonaProtegida()
    xyzonaprotegida4 = zonaprotegida4nivel3.getXYZonaProtegida()


    listaxyzonasprotegidas = getXyZonasProtegidas(xyzonaprotegida1, xyzonaprotegida2, xyzonaprotegida3, xyzonaprotegida4)
    listaxyamenazas = getXyAmenazas(xyamenaza1, xyamenaza2, xyamenaza3, xyamenaza4)

    supertabletnivel3.moverProyectil(nivel3.getGrilla(), listaxyamenazas)
    xyproyectil = supertabletnivel3.getXyProyectil()

    amenaza1nivel3.moverAmenaza(supertabletnivel3.getXyJugador(), xyproyectil)
    amenaza2nivel3.moverAmenaza(supertabletnivel3.getXyJugador(), xyproyectil)
    amenaza3nivel3.moverAmenaza(supertabletnivel3.getXyJugador(), xyproyectil)
    amenaza4nivel3.moverAmenaza(supertabletnivel3.getXyJugador(), xyproyectil)

    zonaprotegida1nivel3.comprobarAmenaza(listaxyamenazas)
    zonaprotegida2nivel3.comprobarAmenaza(listaxyamenazas)
    zonaprotegida3nivel3.comprobarAmenaza(listaxyamenazas)
    zonaprotegida4nivel3.comprobarAmenaza(listaxyamenazas)

    comprobarAmenazaZonaSegura(listaxyzonasprotegidas, "nivel3")

    supertabletnivel3.moverJugador(nivel3.getGrilla(), listaxyamenazas)
    xyjugador = supertabletnivel3.getXyJugador()

    nivel3.dibujarZonaDeTransporte(xyjugador, listaxyamenazas, xyproyectil, listaxyzonasprotegidas)

    comprobarRehacerAmenaza()

    dibujarrectangulofondo(60, 7, 1000, 71)
    textoContadorPasos1 = Texto(100, 23, "Contador de pasos:" + supertabletnivel3.getContadorPasos(40)[0], 30)
    textoContadorPasos1.dibujarTexto()

    textoContadormA = Texto(600, 23, "Contador de mA: " + str(supertabletnivel3.getContadormA()), 30)
    textoContadormA.dibujarTexto()

    botonvolver.dibujarBoton("elegirnivel")

    if supertabletnivel3.getContadormA() <= 0:
        setPantallaActual("reintentarnivel3")
    botonreintentar.dibujarBoton("reintentarnivel3")

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
    cron3.dibujarTiempo()


def comprobarRehacerAmenaza():
    amenaza1nivel3.comprobarRehacer(supertabletnivel3.getMovioAmenaza()[0], supertabletnivel3.getMovioAmenaza()[1],
                                supertabletnivel3.getMovioAmenaza()[2])
    amenaza2nivel3.comprobarRehacer(supertabletnivel3.getMovioAmenaza()[0], supertabletnivel3.getMovioAmenaza()[1],
                                    supertabletnivel3.getMovioAmenaza()[2])
    amenaza3nivel3.comprobarRehacer(supertabletnivel3.getMovioAmenaza()[0], supertabletnivel3.getMovioAmenaza()[1],
                                    supertabletnivel3.getMovioAmenaza()[2])
    amenaza4nivel3.comprobarRehacer(supertabletnivel3.getMovioAmenaza()[0], supertabletnivel3.getMovioAmenaza()[1],
                                    supertabletnivel3.getMovioAmenaza()[2])


def reintentarNivel3():
    nivel3.__init__(10, 10)

    # Jugador (xinicial, yinicial)
    supertabletnivel3.__init__(3, 2)

    # Amenaza (xinicial, yinicial)
    amenaza1nivel3.__init__(3, 3)
    amenaza2nivel3.__init__(4, 5)
    amenaza3nivel3.__init__(5, 3)
    amenaza4nivel3.__init__(6, 6)

    # ZonaProtegida (xinicial, yinicial)
    zonaprotegida1nivel3.__init__(2, 4)
    zonaprotegida2nivel3 .__init__(2, 6)
    zonaprotegida3nivel3.__init__(4, 7)
    zonaprotegida4nivel3.__init__(7, 2)

    #Cronometro reinicio
    cron3.__init__(True, "Arial", 30, 90, 400)

    setPantallaActual("nivel3")
