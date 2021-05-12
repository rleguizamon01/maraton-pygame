import pygame
from Texto import *
from Boton import *
from pantallaNivel1 import *
from pantallaNivel2 import *
from pantallaNivel3 import *
from pantallaElegirNivel import *
from Jugador import *
from Timer import *

textoVictoria = Texto(407, 225, "Derrotaste a la amenaza!", 24)


def dibujarPantallaVictoriaNivel1():
    AZUL = (94, 163, 232)
    GRIS = (150, 150, 150)
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)

    bx = 1152  # Alto de la caja
    by = 648  # Largo de la caja

    file_nombre = 'score_file.txt'
    X = 1152
    Y = 648
    fuente = pygame.font.Font('VCR_OSD_MONO_1.001.ttf', 20)
    pantalla = pygame.display.set_mode((X, Y))

    segundos = cron.getSegundos()
    print("dou  " + str(supertablet.getContadormA()) + "    " + str(segundos))
    mi_puntaje = supertablet.getContadormA() / segundos

    # Encuentra el mayor puntaje y lo compara con el puntaje del usuario
    def encontrar_puntaje_alto(file_nombre):
        file = open(file_nombre, 'r')
        lineas = file.readlines()
        file.close

        puntaje_alto = 0

        # Separa el nombre y el puntaje en diferentes variables
        for line in lineas:
            nombre, puntaje = line.strip().split(",")
            puntaje = int(puntaje)

            # Si el puntaje del usuario es mayor al puntaje lo actual el primero reemplaza al segundo
            if puntaje > puntaje_alto:
                puntaje_alto = puntaje
                nombre_alto = nombre

        return nombre_alto, puntaje_alto

    # Agrega el nombre y el puntaje al archivo .txt
    def agregar_a_file(file_nombre, tu_nombre, puntos):
        file_puntaje = open(file_nombre, 'a')
        file_puntaje.write(tu_nombre + "," + str(puntos) + "\n")
        file_puntaje.close()

    # Dibuja la pantalla que muestra los 10 mejores puntajes
    def mostrar_top10(pantalla, file_nombre):
        bx = 1152  # x-size of caja
        by = 648  # y-size of caja

        file = open(file_nombre, 'r')
        lineas = file.readlines()

        lista_puntajes = []
        for line in lineas:
            sep = line.index(',')
            nombre = line[:sep]
            puntaje = int(line[sep + 1:])
            lista_puntajes.append((puntaje, nombre))
        file.close
        lista_puntajes.sort(reverse=True)  # sort from largest to smallest
        mejor = lista_puntajes[:10]  # top 10 values

        # Hace la pantalla del top 10 puntajes
        caja = pygame.display.set_mode((bx, by))
        bg = pygame.image.load('fondo.png')
        bg = pygame.transform.scale(bg, (1152, 648))
        pantalla.blit(bg, (0, 0))

        pygame.draw.rect(caja, AZUL, (50, 12, bx - 100, 35), 0)  # rectangulo azul de arriba
        pygame.draw.rect(caja, AZUL, (50, by - 60, bx - 100, 42), 0)  # rectangulo azul de abajo

        txt_surf = fuente.render("Puntajes Altos", True, NEGRO)  # Titulo
        txt_rect = txt_surf.get_rect(center=(bx // 2, 30))
        caja.blit(txt_surf, txt_rect)

        txt_surf = fuente.render("Oprime ENTER para continuar", True, NEGRO)  # Texto de la caja de abajo
        txt_rect = txt_surf.get_rect(center=(bx // 2, by - 40))
        caja.blit(txt_surf, txt_rect)

        # Escribe los 10 mejores puntajes en la pantalla
        for i, entry in enumerate(mejor):
            txt_surf = fuente.render(entry[1] + "  " + str(entry[0]), True, NEGRO)
            txt_rect = txt_surf.get_rect(center=(bx // 2, 45 * i + 100))
            caja.blit(txt_surf, txt_rect)

        pantalla.blit(caja, (0, 0))
        pygame.display.flip()


        while True:
            for event in pygame.event.get():
                # Decide que pasa cuando se oprime ENTER en la pantalla de top 10 puntajes
                if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                    reintentarNivel1()
                    setPantallaActual("nivel2")
                    botonnivel2.setPermitirEventos()
                    return
            # Permite visualizar la lista de puntajes por un tiempo luego de slir de la misma
            pygame.time.wait(200)

    # Dibuja la caja en la que se ingresa el nombre del usuario
    def hacercaja(pantalla, txt):
        # Dibuja la caja
        caja = pygame.display.set_mode((bx, by))
        bg = pygame.image.load('fondo.png')
        bg = pygame.transform.scale(bg, (1152, 648))
        pantalla.blit(bg, (0, 0))

        # Escribe el mensaje inicial
        txt_surf = fuente.render(txt, True, NEGRO)
        txt_rect = txt_surf.get_rect(center=(bx // 2, 130))
        caja.blit(txt_surf, txt_rect)

        dibujarTitulo("VICTORIA!")
        dibujarrectangulofondo(140, 170)
        textoVictoria.dibujarTexto()
        dibujarrectangulofondo(140, 370)
        textoContadorPasosVictoria = Texto(280, 425, textoVictoriaPasos(supertablet.getContadorPasos(15), 15), 27)
        textoContadorPasosVictoria.dibujarTexto()



        # Dibuja un punto parpadeante que indica donde se escribe el nombre
        def punto_parpadeante():
            for color in [GRIS, BLANCO]:
                pygame.draw.circle(caja, color, (bx // 2, 90), 7, 0)
                pygame.display.flip()
                pygame.time.wait(300)


        # Muestra el nombre que ingresa el usuario
        def mostrar_nombre(nombre):
            pygame.draw.rect(caja, AZUL, (50, 80, bx - 100, 20), 0)
            txt_surf = fuente.render(nombre, True, NEGRO)
            txt_rect = txt_surf.get_rect(center=(bx // 2, int(90)))
            caja.blit(txt_surf, txt_rect)
            pygame.display.flip()

        nombre = ""
        # Loop para ingresar el nombre
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    inkey = event.key
                    if inkey in [13, 271]:  # Teclas enter/return
                        return nombre
                    elif inkey == 8:  # Tecla backspace
                        nombre = nombre[:-1]
                    elif inkey <= 300:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT and 122 >= inkey >= 97:# Cambia las letras a mayusculas
                            inkey -= 32  # Mayusculas
                        nombre += chr(inkey)  # Agrega al nombre cada caracter que tipee el usuario

            # Decide si se debe dibujar el punto parpadeante o el nombre del usuario
            if nombre == "":
                punto_parpadeante()
            mostrar_nombre(nombre)

    def puntaje_alto(pantalla, file_nombre, tus_puntos):
        nombre_alto, puntaje_alto = encontrar_puntaje_alto(file_nombre)

        st1 = "El puntaje mas alto es "
        st2 = " lo hizo "
        st3 = " Cual es tu nombre?"
        txt = st1 + str(puntaje_alto) + st2 + nombre_alto + st3
        tu_nombre = hacercaja(pantalla, txt)

        if tu_nombre == None or len(tu_nombre) == 0:
            return  # La file no se actualiza si no se da un nombre

        agregar_a_file(file_nombre, tu_nombre, tus_puntos)
        mostrar_top10(pantalla, file_nombre)
        return

    puntaje_alto(pantalla, 'score_file.txt', mi_puntaje)


def dibujarPantallaVictoriaNivel2():
    AZUL = (94, 163, 232)
    GRIS = (150, 150, 150)
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)

    bx = 1152  # Alto de la caja
    by = 648  # Largo de la caja

    file_nombre = 'score_file.txt'
    X = 1152
    Y = 648
    fuente = pygame.font.Font('VCR_OSD_MONO_1.001.ttf', 20)
    pantalla = pygame.display.set_mode((X, Y))

    mi_puntaje = supertablet.getContadormA()

    # Encuentra el mayor puntaje y lo compara con el puntaje del usuario
    def encontrar_puntaje_alto(file_nombre):
        file = open(file_nombre, 'r')
        lineas = file.readlines()
        file.close

        puntaje_alto = 0

        # Separa el nombre y el puntaje en diferentes variables
        for line in lineas:
            nombre, puntaje = line.strip().split(",")
            puntaje = int(puntaje)

            # Si el puntaje del usuario es mayor al puntaje lo actual el primero reemplaza al segundo
            if puntaje > puntaje_alto:
                puntaje_alto = puntaje
                nombre_alto = nombre

        return nombre_alto, puntaje_alto

    # Agrega el nombre y el puntaje al archivo .txt
    def agregar_a_file(file_nombre, tu_nombre, puntos):
        file_puntaje = open(file_nombre, 'a')
        file_puntaje.write(tu_nombre + "," + str(puntos) + "\n")
        file_puntaje.close()

    # Dibuja la pantalla que muestra los 10 mejores puntajes
    def mostrar_top10(pantalla, file_nombre):
        bx = 1152  # x-size of caja
        by = 648  # y-size of caja

        file = open(file_nombre, 'r')
        lineas = file.readlines()

        lista_puntajes = []
        for line in lineas:
            sep = line.index(',')
            nombre = line[:sep]
            puntaje = int(line[sep + 1:])
            lista_puntajes.append((puntaje, nombre))
        file.close
        lista_puntajes.sort(reverse=True)  # sort from largest to smallest
        mejor = lista_puntajes[:10]  # top 10 values

        # Hace la pantalla del top 10 puntajes
        caja = pygame.display.set_mode((bx, by))
        bg = pygame.image.load('fondo.png')
        bg = pygame.transform.scale(bg, (1152, 648))
        pantalla.blit(bg, (0, 0))

        pygame.draw.rect(caja, AZUL, (50, 12, bx - 100, 35), 0)  # rectangulo azul de arriba
        pygame.draw.rect(caja, AZUL, (50, by - 60, bx - 100, 42), 0)  # rectangulo azul de abajo

        txt_surf = fuente.render("Puntajes Altos", True, NEGRO)  # Titulo
        txt_rect = txt_surf.get_rect(center=(bx // 2, 30))
        caja.blit(txt_surf, txt_rect)

        txt_surf = fuente.render("Oprime ENTER para continuar", True, NEGRO)  # Texto de la caja de abajo
        txt_rect = txt_surf.get_rect(center=(bx // 2, by - 40))
        caja.blit(txt_surf, txt_rect)

        # Escribe los 10 mejores puntajes en la pantalla
        for i, entry in enumerate(mejor):
            txt_surf = fuente.render(entry[1] + "  " + str(entry[0]), True, NEGRO)
            txt_rect = txt_surf.get_rect(center=(bx // 2, 45 * i + 100))
            caja.blit(txt_surf, txt_rect)

        pantalla.blit(caja, (0, 0))
        pygame.display.flip()


        while True:
            for event in pygame.event.get():
                # Decide que pasa cuando se oprime ENTER en la pantalla de top 10 puntajes
                if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                    reintentarNivel2()
                    setPantallaActual("nivel3")
                    botonnivel3.setPermitirEventos()
                    return
            # Permite visualizar la lista de puntajes por un tiempo luego de slir de la misma
            pygame.time.wait(200)

    # Dibuja la caja en la que se ingresa el nombre del usuario
    def hacercaja(pantalla, txt):
        # Dibuja la caja
        caja = pygame.display.set_mode((bx, by))
        bg = pygame.image.load('fondo.png')
        bg = pygame.transform.scale(bg, (1152, 648))
        pantalla.blit(bg, (0, 0))

        # Escribe el mensaje inicial
        txt_surf = fuente.render(txt, True, NEGRO)
        txt_rect = txt_surf.get_rect(center=(bx // 2, 130))
        caja.blit(txt_surf, txt_rect)

        dibujarTitulo("VICTORIA!")
        dibujarrectangulofondo(140, 170)
        textoVictoria.dibujarTexto()
        dibujarrectangulofondo(140, 370)
        textoContadorPasosVictoria = Texto(280, 425, textoVictoriaPasos(supertabletnivel2.getContadorPasos(60), 60), 27)
        textoContadorPasosVictoria.dibujarTexto()

        # Dibuja un punto parpadeante que indica donde se escribe el nombre
        def punto_parpadeante():
            for color in [GRIS, BLANCO]:
                pygame.draw.circle(caja, color, (bx // 2, 90), 7, 0)
                pygame.display.flip()
                pygame.time.wait(300)

        # Muestra el nombre que ingresa el usuario
        def mostrar_nombre(nombre):
            pygame.draw.rect(caja, AZUL, (50, 80, bx - 100, 20), 0)
            txt_surf = fuente.render(nombre, True, NEGRO)
            txt_rect = txt_surf.get_rect(center=(bx // 2, int(90)))
            caja.blit(txt_surf, txt_rect)
            pygame.display.flip()

        nombre = ""
        # Loop para ingresar el nombre
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    inkey = event.key
                    if inkey in [13, 271]:  # Teclas enter/return
                        return nombre
                    elif inkey == 8:  # Tecla backspace
                        nombre = nombre[:-1]
                    elif inkey <= 300:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT and 122 >= inkey >= 97: # Cambia las letras a mayusculas
                            inkey -= 32  # Mayusculas
                        nombre += chr(inkey)  # Agrega al nombre cada caracter que tipee el usuario

            # Decide si se debe dibujar el punto parpadeante o el nombre del usuario
            if nombre == "":
                punto_parpadeante()
            mostrar_nombre(nombre)

    def puntaje_alto(pantalla, file_nombre, tus_puntos):
        nombre_alto, puntaje_alto = encontrar_puntaje_alto(file_nombre)

        st1 = "El puntaje mas alto del nivel 2 es: "
        st2 = " lo hizo "
        st3 = " Cual es tu nombre?"
        txt = st1 + str(puntaje_alto) + st2 + nombre_alto + st3
        tu_nombre = hacercaja(pantalla, txt)

        if tu_nombre == None or len(tu_nombre) == 0:
            return  # La file no se actualiza si no se da un nombre

        agregar_a_file(file_nombre, tu_nombre, tus_puntos)
        mostrar_top10(pantalla, file_nombre)
        return

    puntaje_alto(pantalla, 'score_file_nivel2.txt', mi_puntaje)

def dibujarPantallaVictoriaNivel3():
    AZUL = (94, 163, 232)
    GRIS = (150, 150, 150)
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)

    bx = 1152  # Alto de la caja
    by = 648  # Largo de la caja

    file_nombre = 'score_file_nivel3.txt'
    X = 1152
    Y = 648
    fuente = pygame.font.Font('VCR_OSD_MONO_1.001.ttf', 20)
    pantalla = pygame.display.set_mode((X, Y))

    mi_puntaje = supertablet.getContadormA()

    # Encuentra el mayor puntaje y lo compara con el puntaje del usuario
    def encontrar_puntaje_alto(file_nombre):
        file = open(file_nombre, 'r')
        lineas = file.readlines()
        file.close

        puntaje_alto = 0

        # Separa el nombre y el puntaje en diferentes variables
        for line in lineas:
            nombre, puntaje = line.strip().split(",")
            puntaje = int(puntaje)

            # Si el puntaje del usuario es mayor al puntaje lo actual el primero reemplaza al segundo
            if puntaje > puntaje_alto:
                puntaje_alto = puntaje
                nombre_alto = nombre

        return nombre_alto, puntaje_alto

    # Agrega el nombre y el puntaje al archivo .txt
    def agregar_a_file(file_nombre, tu_nombre, puntos):
        file_puntaje = open(file_nombre, 'a')
        file_puntaje.write(tu_nombre + "," + str(puntos) + "\n")
        file_puntaje.close()

    # Dibuja la pantalla que muestra los 10 mejores puntajes
    def mostrar_top10(pantalla, file_nombre):
        bx = 1152  # x-size of caja
        by = 648  # y-size of caja

        file = open(file_nombre, 'r')
        lineas = file.readlines()

        lista_puntajes = []
        for line in lineas:
            sep = line.index(',')
            nombre = line[:sep]
            puntaje = int(line[sep + 1:])
            lista_puntajes.append((puntaje, nombre))
        file.close
        lista_puntajes.sort(reverse=True)  # sort from largest to smallest
        mejor = lista_puntajes[:10]  # top 10 values

        # Hace la pantalla del top 10 puntajes
        caja = pygame.display.set_mode((bx, by))
        bg = pygame.image.load('fondo.png')
        bg = pygame.transform.scale(bg, (1152, 648))
        pantalla.blit(bg, (0, 0))

        pygame.draw.rect(caja, AZUL, (50, 12, bx - 100, 35), 0)  # rectangulo azul de arriba
        pygame.draw.rect(caja, AZUL, (50, by - 60, bx - 100, 42), 0)  # rectangulo azul de abajo

        txt_surf = fuente.render("Puntajes Altos", True, NEGRO)  # Titulo
        txt_rect = txt_surf.get_rect(center=(bx // 2, 30))
        caja.blit(txt_surf, txt_rect)

        txt_surf = fuente.render("Oprime ENTER para continuar", True, NEGRO)  # Texto de la caja de abajo
        txt_rect = txt_surf.get_rect(center=(bx // 2, by - 40))
        caja.blit(txt_surf, txt_rect)

        # Escribe los 10 mejores puntajes en la pantalla
        for i, entry in enumerate(mejor):
            txt_surf = fuente.render(entry[1] + "  " + str(entry[0]), True, NEGRO)
            txt_rect = txt_surf.get_rect(center=(bx // 2, 45 * i + 100))
            caja.blit(txt_surf, txt_rect)

        pantalla.blit(caja, (0, 0))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                # Decide que pasa cuando se oprime ENTER en la pantalla de top 10 puntajes
                if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                    pygame.quit()
                    return
            # Permite visualizar la lista de puntajes por un tiempo luego de slir de la misma
            pygame.time.wait(200)

    # Dibuja la caja en la que se ingresa el nombre del usuario
    def hacercaja(pantalla, txt):
        # Dibuja la caja
        caja = pygame.display.set_mode((bx, by))
        bg = pygame.image.load('fondo.png')
        bg = pygame.transform.scale(bg, (1152, 648))
        pantalla.blit(bg, (0, 0))

        # Escribe el mensaje inicial
        txt_surf = fuente.render(txt, True, NEGRO)
        txt_rect = txt_surf.get_rect(center=(bx // 2, 130))
        caja.blit(txt_surf, txt_rect)

        dibujarTitulo("VICTORIA!")
        dibujarrectangulofondo(140, 170)
        textoVictoria.dibujarTexto()
        dibujarrectangulofondo(140, 370)
        textoContadorPasosVictoria = Texto(280, 425, textoVictoriaPasos(supertabletnivel3.getContadorPasos(40), 40), 27)
        textoContadorPasosVictoria.dibujarTexto()

        # Dibuja un punto parpadeante que indica donde se escribe el nombre
        def punto_parpadeante():
            for color in [GRIS, BLANCO]:
                pygame.draw.circle(caja, color, (bx // 2, 90), 7, 0)
                pygame.display.flip()
                pygame.time.wait(300)

        # Muestra el nombre que ingresa el usuario
        def mostrar_nombre(nombre):
            pygame.draw.rect(caja, AZUL, (50, 80, bx - 100, 20), 0)
            txt_surf = fuente.render(nombre, True, NEGRO)
            txt_rect = txt_surf.get_rect(center=(bx // 2, int(90)))
            caja.blit(txt_surf, txt_rect)
            pygame.display.flip()

        nombre = ""
        # Loop para ingresar el nombre
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    inkey = event.key
                    if inkey in [13, 271]:  # Teclas enter/return
                        return nombre
                    elif inkey == 8:  # Tecla backspace
                        nombre = nombre[:-1]
                    elif inkey <= 300:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT and 122 >= inkey >= 97:# Cambia las letras a mayusculas
                            inkey -= 32  # Mayusculas
                        nombre += chr(inkey)  # Agrega al nombre cada caracter que tipee el usuario

            # Decide si se debe dibujar el punto parpadeante o el nombre del usuario
            if nombre == "":
                punto_parpadeante()
            mostrar_nombre(nombre)

    def puntaje_alto(pantalla, file_nombre, tus_puntos):
        nombre_alto, puntaje_alto = encontrar_puntaje_alto(file_nombre)

        st1 = "El puntaje mas alto es del nivel 3 es: "
        st2 = " lo hizo "
        st3 = " Cual es tu nombre?"
        txt = st1 + str(puntaje_alto) + st2 + nombre_alto + st3
        tu_nombre = hacercaja(pantalla, txt)

        if tu_nombre == None or len(tu_nombre) == 0:
            return  # La file no se actualiza si no se da un nombre

        agregar_a_file(file_nombre, tu_nombre, tus_puntos)
        mostrar_top10(pantalla, file_nombre)
        return

    puntaje_alto(pantalla, 'score_file_nivel3.txt', mi_puntaje)
