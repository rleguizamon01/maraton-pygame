import pygame
from imagenes import *
from configuracion import *


class Grilla(object):
    def __init__(self, anchogrilla, altogrilla):
        # Elige la cantidad de casillas que va haber por lado
        self.anchogrilla = anchogrilla
        self.altogrilla = altogrilla
        # Elige la cantidad de pixeles por casilla
        self.cantPixelesPorLadoCasilla = cantPixelesPorLadoCasilla
        self.zonaDeTransporte = [[0 for x in range(self.altogrilla + 1)] for y in
                                 range(self.anchogrilla + 1)]
        self.margenizq = 200

    def crearZonaDeTransporte(self):
        # Su funcion es setear la posicion de las paredes y devolver self.zonaDeTransporte
        # con las paredes incluidas

        for y in range(1, self.anchogrilla + 1):
            for x in range(1, self.altogrilla + 1):
                self.zonaDeTransporte[1][x] = 'pared'
                self.zonaDeTransporte[self.anchogrilla][x] = 'pared'
                self.zonaDeTransporte[y][1] = 'pared'
                self.zonaDeTransporte[y][self.altogrilla] = 'pared'


        return self.zonaDeTransporte

    def borrarElemento(self, xy):
        # Borra cualquier elemento en la posicion [x][y] de la matriz
        self.zonaDeTransporte[xy[0]][xy[1]] = 0

    def posicionarElemento(self, elemento, xy):
        # Posiciona un elemento a eleccion en la posicion [x][y]
        self.zonaDeTransporte[xy[0]][xy[1]] = elemento

    def dibujarZonaDeTransporte(self, xyjugador, listaxycorazonesamenaza, xydisparo, listaxyzonasprotegidas):
        # Posiciona al jugador, a la amenaza, a los disparos y a la zona protegida segun los parametros xyjugador,
        # xyamenaza, xydisparo y xyzonaprotegida Todos son una tupla, o sea tiene dos valores xyjugador = (x,
        # y) que pueden ser llamados individualmente segun la posicion en la lista xyjugador[0] es unicamente la x
        # xyjugador[1] es unicamente la y los valores son conseguidos por los metodos get() de cada clase y llamados
        # a esta funcion mediante parametros en DibujarTodo()

        # Incluye las paredes en self.zonaDeTransporte
        self.zonaDeTransporte = self.crearZonaDeTransporte()

        # Dibuja el fondo de la grilla
        ventana.blit(imgPiso, (self.margenizq + self.cantPixelesPorLadoCasilla, self.cantPixelesPorLadoCasilla))

        # Dibuja distintas imagenes de las amenazas segun su cantidad de corazones
        self.posicionarElemento('disparo', (xydisparo[0], xydisparo[1]))

        # Dibuja los disparos, la zonaprotegida y al jugador en las coordenadas llamadas en los parametros
        for i in range(0, len(listaxyzonasprotegidas)):

            self.posicionarElemento('zonaprotegida', (listaxyzonasprotegidas[i][0]))

        self.posicionarElemento('jugador', (xyjugador[0][0], xyjugador[0][1]))

        for i in range(0, len(listaxycorazonesamenaza)):

            if listaxycorazonesamenaza[i][1] == 3:
                self.posicionarElemento('amenaza_3corazon', listaxycorazonesamenaza[i][0])
            elif listaxycorazonesamenaza[i][1] == 2:
                self.posicionarElemento('amenaza_2corazon', listaxycorazonesamenaza[i][0])
            if listaxycorazonesamenaza[i][1] == 1:
                self.posicionarElemento('amenaza_1corazon', listaxycorazonesamenaza[i][0])
            elif listaxycorazonesamenaza[i][1] == 0:
                self.posicionarElemento('amenaza_0corazon', listaxycorazonesamenaza[i][0])

        # Dibuja cada elemento mediante el uso de for anidados para recorrer la matriz
        for i in range(1, self.altogrilla + 1):
            for j in range(1, self.anchogrilla + 1):
                # Verifica el valor en la matriz
                if self.zonaDeTransporte[j][i] == 'disparo':
                    ventana.blit(imgDisparo, (self.margenizq + self.cantPixelesPorLadoCasilla * j, self.cantPixelesPorLadoCasilla * i))
                if self.zonaDeTransporte[j][i] == 'zonaprotegida':
                    ventana.blit(imgAreaProtegida,
                                 (self.margenizq + self.cantPixelesPorLadoCasilla * j, self.cantPixelesPorLadoCasilla * i))
                if self.zonaDeTransporte[j][i] == 'jugador':
                    ventana.blit(imgSuperTablet,
                                 (self.margenizq + self.cantPixelesPorLadoCasilla * j, self.cantPixelesPorLadoCasilla * i))
                if self.zonaDeTransporte[j][i] == 'pared':
                    ventana.blit(imgPared, (self.margenizq + self.cantPixelesPorLadoCasilla * j, self.cantPixelesPorLadoCasilla * i))

                if self.zonaDeTransporte[j][i] == 'amenaza_3corazon':
                    ventana.blit(listaAmenazas4[0],
                                 (self.margenizq + self.cantPixelesPorLadoCasilla * j, self.cantPixelesPorLadoCasilla * i))
                if self.zonaDeTransporte[j][i] == 'amenaza_2corazon':
                    ventana.blit(listaAmenazas4[1],
                                 (self.margenizq + self.cantPixelesPorLadoCasilla * j, self.cantPixelesPorLadoCasilla * i))
                if self.zonaDeTransporte[j][i] == 'amenaza_1corazon':
                    ventana.blit(listaAmenazas4[2],
                                 (self.margenizq + self.cantPixelesPorLadoCasilla * j, self.cantPixelesPorLadoCasilla * i))
                if self.zonaDeTransporte[j][i] == 'amenaza_0corazon':
                    ventana.blit(listaAmenazas4[3],
                                 (self.margenizq + self.cantPixelesPorLadoCasilla * j, self.cantPixelesPorLadoCasilla * i))

        # Al terminar el metodo, borra las posiciones actuales de los jugadores y la amenaza
        self.borrarElemento((xyjugador[0][0], xyjugador[0][1]))
        for i in range(0, len(listaxycorazonesamenaza)):
            self.borrarElemento(listaxycorazonesamenaza[i][0])
        self.borrarElemento((xydisparo[0], xydisparo[1]))

    def getGrilla(self):
        # Devuelve la tupla zonaDeTransporte si es llamada por fuera de la clase
        return self.zonaDeTransporte

    def setParedes(self, x, y):
        self.posicionarElemento("pared", (x, y))

    def setPixelesLadoCasilla(self, pixeles):
        self.cantPixelesPorLadoCasilla = pixeles
