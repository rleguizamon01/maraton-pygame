import pygame
from eventos import *
from sonidos import *


class Jugador(object):
    def __init__(self, xjugador, yjugador):
        # Solicita la posicion inicial de Supertablet mediante xjugador e yjugador
        self.xjugador = xjugador
        self.yjugador = yjugador

        # Los proyectiles de Supertablet permanecen en (0, 0) hasta ser utilizados
        self.xproyectil = 0
        self.yproyectil = 0

        # Supertablet comienza sin estar disparando
        self.estadisparando = False

        # Por defecto, se toma que la direccion en la que Supertablet dispararia por primera vez
        # si no se movio, es hacia la derecha
        self.ultladomovimiento = (1, 0)

        self.ladomovimiento = (0, 0)

        # Cuanta la cantidad de pasos de Supertablet
        self.contadorPasos = 0

        self.contadormA = 7000
        self.movioamenaza = False
        self.xyamenazamovida = 0, 0

    def puedeMover(self, x, y, xdoble, ydoble, grilla, listaxyamenazas):
        # si hay una pared en la direccion que se desea mover, la funcion booleana puedeMover() devuelve falso
        self.movioamenaza = False
        if grilla[self.xjugador + x][self.yjugador + y] == 'pared':
            return False
        # si hay una amenaza derrotada en la direccion que se desea mover, se comprueba si tambien hay una pared a
        # dos bloques de distancia en la misma direccion (si ambas se cumplen la funcion devuelve False)
        else:
            for i in range(0, len(listaxyamenazas)):
                if listaxyamenazas[i][0] == (self.xjugador + x, self.yjugador + y):
                    if grilla[self.xjugador + xdoble][self.yjugador + ydoble] == 'pared':
                        return False
                    else:
                        for c in range(0, len(listaxyamenazas)):
                            if listaxyamenazas[c][0] == (self.xjugador + xdoble, self.yjugador + ydoble):
                                self.contadormA -= 200
                                return False
                        self.contadormA -= 5
                        self.movioamenaza = True
                        self.xyamenazamovida = (self.xjugador + xdoble, self.yjugador + ydoble)
        return True

    def moverJugador(self, grilla, listaxyamenazas):
        # El metodo solicita la lista de la grilla y la posicion de la amenaza

        self.ladomovimiento = (0, 0)

        # si la tecla presionada es (...) y la funcion puedeMover() es verdadera, el jugador se mueve a esa direccion
        # La tabla de como cambia x e y cuando se produce un movimiento hacia cierta direccion es: direccion del
        # movimiento = (x, y) izquierda = (-1, 0) derecha = (1, 0) arriba = (0, -1) abajo = (0, 1) El tercer y cuarto
        # parametro son el primero y el segundo multiplicados por dos. Se usan para el puedeMover() en el momento que
        # busca si hay una pared a dos de distancia cuando tiene una amenaza al frente

        if getEventoTecla() == "LEFT" and self.puedeMover(-1, 0, -2, 0, grilla, listaxyamenazas):
            self.xjugador += -1
            self.yjugador += 0
            self.ladomovimiento = (-1, 0)
            if not self.estadisparando:
                self.ultladomovimiento = (-1, 0)
            self.contadorPasos += 1
            self.contadormA -= 10
            self.apretarUnaVezRehacer = True

        if getEventoTecla() == "RIGHT" and self.puedeMover(1, 0, 2, 0, grilla, listaxyamenazas):
            self.xjugador += 1
            self.yjugador += 0
            self.ladomovimiento = (1, 0)
            if not self.estadisparando:
                self.ultladomovimiento = (1, 0)
            self.contadorPasos += 1
            self.contadormA -= 10
            self.apretarUnaVezRehacer = True

        if getEventoTecla() == "UP" and self.puedeMover(0, -1, 0, -2, grilla, listaxyamenazas):
            self.xjugador += 0
            self.yjugador += -1
            self.ladomovimiento = (0, -1)
            if not self.estadisparando:
                self.ultladomovimiento = (0, -1)
            self.contadorPasos += 1
            self.contadormA -= 10
            self.apretarUnaVezRehacer = True

        if getEventoTecla() == "DOWN" and self.puedeMover(0, 1, 0, 2, grilla, listaxyamenazas):
            self.xjugador += 0
            self.yjugador += 1
            self.ladomovimiento = (0, 1)
            if not self.estadisparando:
                self.ultladomovimiento = (0, 1)
            self.contadorPasos += 1
            self.contadormA -= 10
            self.apretarUnaVezRehacer = True

        if getEventoTecla() == "x" and self.apretarUnaVezRehacer:
            self.xjugador += self.ultladomovimiento[0] * -1
            self.yjugador += self.ultladomovimiento[1] * -1
            self.contadormA += 10
            self.apretarUnaVezRehacer = False
            if self.movioamenaza:
                self.contadormA += 5
            self.contadorPasos -= 1

    # Proyectil
    def moverProyectil(self, grilla, listaxyamenazas):
        # El metodo solicita la lista de la grilla y la posicion de la amenaza

        # Si se presiona la tecla "d" y Supertablet no esta disparando, comienza a disparar, el proyectil
        # toma la posicion de Supertablet y, si sonido esta en ON, se reproduce un sonido de disparo
        if getEventoTecla() == "d":
            if not self.estadisparando:
                self.contadormA -= 10
                self.estadisparando = True
                self.xproyectil = self.xjugador
                self.yproyectil = self.yjugador
                if getSonidoVolumen():
                    sonidoDisparo.play()

        # Si se presiona "d" y no hay una pared en frente en el sentido en el que se movio por ultima vez,
        # la bala se mueve en la direccion que se movio por ultima vez hasta colisionar con una amenaza o pared
        if self.estadisparando:
            if self.ultladomovimiento == (-1, 0) and self.puedeDisparar(-1, 0, listaxyamenazas, grilla):
                self.xproyectil += -1
                self.yproyectil += 0
            elif self.ultladomovimiento == (1, 0) and self.puedeDisparar(1, 0, listaxyamenazas, grilla):
                self.xproyectil += 1
                self.yproyectil += 0
            elif self.ultladomovimiento == (0, -1) and self.puedeDisparar(0, -1, listaxyamenazas, grilla):
                self.xproyectil += 0
                self.yproyectil += -1
            elif self.ultladomovimiento == (0, 1) and self.puedeDisparar(0, 1, listaxyamenazas, grilla):
                self.xproyectil += 0
                self.yproyectil += 1
            else:
                self.xproyectil = 0
                self.yproyectil = 0
                self.estadisparando = False

        return self.xproyectil, self.yproyectil, self.estadisparando

    def puedeDisparar(self, x, y, listaxyamenaza, grilla):
        # Si va a haber una pared o amenaza en el proximo movimiento del proyectil, el metodo devuelve False
        if grilla[self.xproyectil + x][self.yproyectil + y] == 'pared':
            return False
        else:
            for i in range(0, len(listaxyamenaza)):
                if listaxyamenaza[i][0] == (self.xproyectil, self.yproyectil):
                    if getSonidoVolumen():
                        sonidoImpacto.play()
                    return False
        return True

    def getXyJugador(self):
        return (self.xjugador, self.yjugador), self.ladomovimiento

    def getXyProyectil(self):
        return self.xproyectil, self.yproyectil

    def getContadormA(self):
        return self.contadormA

    def getContadorPasos(self, cantpasos):
        # Devuelve la cantidad de pasos realizados por SuperTablet
        return str(self.contadorPasos) + "/" + str(cantpasos), self.contadorPasos

    def getMovioAmenaza(self):
        if getEventoTecla() == "x" and self.movioamenaza:
            return True, self.ultladomovimiento, self.xyamenazamovida
        else:
            return False, 0, 0
