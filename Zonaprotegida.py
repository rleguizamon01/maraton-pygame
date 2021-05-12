import pygame
from sonidos import *
from pantallas import *


class Zonaprotegida(object):
    def __init__(self, xzonaprotegida, yzonaprotegida):
        # Solicita mediante los parametros la posicion x e y que se posicionara inicialmente en la matriz
        self.xzonaprotegida = xzonaprotegida
        self.yzonaprotegida = yzonaprotegida
        # Al comenzar la clase la amenaza nunca estara en la Zona Protegida, por lo que el boolean es False
        self.amenazaenzona = False

    def comprobarAmenaza(self, listaxyamenazas):
        # Comprueba si la amenaza esta en la Zona Protegida o no y retorna un boolean
        self.amenazaenzona = False
        for i in range(0, len(listaxyamenazas)):
            if listaxyamenazas[i][0] == (self.xzonaprotegida, self.yzonaprotegida):
                self.amenazaenzona = True

    def getXYZonaProtegida(self):
        return (self.xzonaprotegida, self.yzonaprotegida), self.amenazaenzona

#############

def getXyZonasProtegidas(zonaprotegida1, zonaprotegida2=None, zonaprotegida3=None, zonaprotegida4=None,
                         zonaprotegida5=None):
    listaxyzonasprotegidas = [zonaprotegida1]
    if zonaprotegida2:
        listaxyzonasprotegidas.append(zonaprotegida2)
    if zonaprotegida3:
        listaxyzonasprotegidas.append(zonaprotegida3)
    if zonaprotegida4:
        listaxyzonasprotegidas.append(zonaprotegida4)
    if zonaprotegida5:
        listaxyzonasprotegidas.append(zonaprotegida5)

    return listaxyzonasprotegidas


def comprobarAmenazaZonaSegura(listaxyzonasprotegidas, nivel):
    for i in range(0, len(listaxyzonasprotegidas)):
        if not listaxyzonasprotegidas[i][1]:
            return False

    setPantallaActual("victoria" + nivel)
    if getSonidoVolumen():
        sonidoVictoria.play()
