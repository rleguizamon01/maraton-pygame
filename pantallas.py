import pygame

pantallaActual = "menuprincipal"


def setPantallaActual(valor):
    global pantallaActual
    pantallaActual = valor


def getPantallaActual():
    return pantallaActual
