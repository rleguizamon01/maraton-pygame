import pygame
import sys
from configuracion import ventana
from pantallas import *

class Time(object):
    def __init__(self, condicionPausa, fuent, tamanoletra, x, y):
        #Solicita la condicion para que se mantenga o no en funcionamiento el cronometro y la fuente y tamano con el que sera mostrado en pantalla

        self.condicionPausa = condicionPausa
        self.letra = fuent
        self.tamanoletra = tamanoletra
        self.fuente         = pygame.font.SysFont(self.letra, self.tamanoletra)
        self.tiempo = 0
        self.tiempoinicio = 0
        self.sec            = 0
        self.segundos       = 0
        self.minutos        = 0
        self.stmin = ""
        self.stseg = ""
        self.x = x
        self.y = y
        self.ejecutarTiempoInicio = True
        self.tiempootrapantalla = 0
        self.volverpantalla = False
        self.tiempoactualvuelta = 0

    def dibujarTiempo(self):

        if self.ejecutarTiempoInicio:
            self.tiempoinicio = pygame.time.get_ticks() / 1000
            self.ejecutarTiempoInicio = False

        # En caso de haber empezado a jugar, el cronometro se habra inicializado

        if self.condicionPausa:

            self.tiempo = pygame.time.get_ticks() / 1000 - self.tiempoinicio
            self.sec += self.tiempo

            if self.tiempootrapantalla > 0:
                self.tiempo -= pygame.time.get_ticks() / 1000 - self.tiempootrapantalla
                self.tiempootrapantalla = 0

            self.segundos = self.tiempo % 60
            self.minutos = self.tiempo / 60
            self.stseg = str(self.segundos)
            self.stmin = str(self.minutos)

            if self.segundos % 60 <= 9:
                self.stseg = "0" + self.stseg

            if self.minutos < 10:
                self.stmin = "0" + self.stmin

            self.contador = self.fuente.render(" Tiempo = " + self.stmin + ":" + self.stseg, 0, (0, 0, 0))
            ventana.blit(self.contador, (self.x, self.y))


    def getSegundos(self):
        return self.tiempo
