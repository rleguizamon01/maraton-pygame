import pygame
from configuracion import ventana
from imagenes import *
from eventos import *


class GrillaScrolling(object):
    def __init__(self):
        self.ladogrilla = 6
        self.puntoinicialx = 2
        self.puntoinicialy = 2
        self.anchovision = 5
        self.altovision = 5
        self.cantPixelesPorCasilla = 72
        self.margenizq = 150
        self.zonaDeTransporte = [[0 for x in range(self.ladogrilla + 1)] for y in
                                 range(self.ladogrilla + 1)]

    def dibujarGrillaScrolling(self, xyjugador, xyamenaza, xydisparo):

        self.posicionarElemento('disparo', xydisparo[0], xydisparo[1])
        self.posicionarElemento('jugador', xyjugador[0], xyjugador[1])

        for i in range(1, (self.ladogrilla + 1)):
            self.zonaDeTransporte[i][1] = 'pared'
            self.zonaDeTransporte[i][self.ladogrilla] = 'pared'
            self.zonaDeTransporte[1][i] = 'pared'
            self.zonaDeTransporte[self.ladogrilla][i] = 'pared'

        #ventana.blit(imgPiso, (self.margenizq + self.cantPixelesPorCasilla, self.cantPixelesPorCasilla))

        for i in range(self.puntoinicialx, self.puntoinicialx + self.anchovision):
            for j in range(self.puntoinicialy,  self.puntoinicialy + self.altovision):
                if self.zonaDeTransporte[i][j] == 0:
                    ventana.blit(rectanguloazul, (self.margenizq + self.cantPixelesPorCasilla * j, self.cantPixelesPorCasilla * i))
                if self.zonaDeTransporte[i][j] == 'pared':
                    ventana.blit(imgPared,
                                 (self.margenizq + self.cantPixelesPorCasilla * j, self.cantPixelesPorCasilla * i))
                if self.zonaDeTransporte[i][j] == 'jugador':
                    ventana.blit(imgSuperTablet,
                                 (self.margenizq + self.cantPixelesPorCasilla * j,
                                  self.cantPixelesPorCasilla * i))

        self.borrarElemento(xyjugador[0], xyjugador[1])
        self.borrarElemento(xyamenaza[0], xyamenaza[1])
        self.borrarElemento(xydisparo[0], xydisparo[1])

        self.scrollGrilla()


    def scrollGrilla(self):
        if getEventoTecla() == "RIGHT" and self.puntoinicialx <= (self.ladogrilla - self.anchovision):
            self.puntoinicialx += 1
        if getEventoTecla() == "LEFT" and self.puntoinicialx >= (self.ladogrilla - self.anchovision):
            self.puntoinicialx -= 1
        if getEventoTecla() == "DOWN" and self.puntoinicialy <= (self.ladogrilla - self.altovision):
            self.puntoinicialy += 1
        if getEventoTecla() == "UP" and self.puntoinicialy >= (self.ladogrilla - self.altovision):
            self.puntoinicialy -= 1

    def borrarElemento(self, x, y):
        # Borra cualquier elemento en la posicion [x][y] de la matriz
        self.zonaDeTransporte[x][y] = 0

    def posicionarElemento(self, elemento, x, y):
        # Posiciona un elemento a eleccion en la posicion [x][y]
        self.zonaDeTransporte[x][y] = elemento


    def getGrilla(self):
        # Devuelve la tupla zonaDeTransporte si es llamada por fuera de la clase
        return self.zonaDeTransporte


