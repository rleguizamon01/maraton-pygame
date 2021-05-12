import pygame

run = True
eventotecla = ""
eventomouse = ""


def getEventos():
    global eventomouse
    global eventotecla
    global run

    for event in pygame.event.get():
        # Cerrar ventana
        if event.type == pygame.QUIT:
            run = False
        # Le da un distinto valor a la variable global eventotecla y eventomouse segun el evento ejecutado por el
        # jugador
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                eventotecla = "LEFT"
            if event.key == pygame.K_RIGHT:
                eventotecla = "RIGHT"
            if event.key == pygame.K_UP:
                eventotecla = "UP"
            if event.key == pygame.K_DOWN:
                eventotecla = "DOWN"
            if event.key == pygame.K_d:
                eventotecla = "d"
            if event.key == pygame.K_x:
                eventotecla = "x"
        if event.type == pygame.MOUSEBUTTONDOWN:
            eventomouse = "MOUSEBUTTONDOWN"
        if event.type == pygame.MOUSEBUTTONUP:
            eventomouse = "MOUSEBUTTONUP"
        if event.type == pygame.MOUSEMOTION:
            eventomouse = "MOUSEMOTION"


def getEventoMouse():
    return eventomouse


def getEventoTecla():
    return eventotecla


def setEventos(valor):
    global eventotecla
    global eventomouse

    eventotecla = valor
    eventomouse = valor


def run():
    return run
