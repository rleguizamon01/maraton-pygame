import pygame
from eventos import *
from sonidos import *
from configuracion import *
from pantallas import *

# Listas de colores para botones [(normal), (hover), (presionado)]
coloresazules = [(102, 178, 255), (94, 163, 232), (82, 141, 201)]
coloresverdes = [(68, 186, 100), (60, 159, 87), (53, 138, 76)]
coloresrojos = [(185, 81, 92), (155, 68, 77), (132, 60, 67)]
coloresgrises = [(110, 110, 110), (98, 98, 98), (110, 110, 110)]

class Boton(object):
    # Crea un boton y su comportamiento cambia segun los eventos del mouse
    def __init__(self, permitireventos, tamletra, x, y, width, height, text, colores, coloresOFF=None, textoOFF=None):
        # Los parametros requeridos son el tamano de letra del texto, la posicion en x del boton, la posicion en y,
        # el ancho del boton, el alto, el texto y una lista de colores (el primer color representa el color normal,
        # el segundo cuando el mouse pasa por encima y el tercero cuando el mouse lo presiona).
        # Los parametros opcionales son para los botones ON/OFF. ColoresOFF representa la lista de colores
        # cuando el boton fue apretado y cambio de ON a OFF y textoOFF es el texto que se muestra cuando el
        # boton esta en OFF.
        self.permitireventos = permitireventos
        self.ventana = ventana
        self.tamletra = tamletra
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.colores = colores
        self.coloresOFF = coloresOFF
        self.textoOFF = textoOFF

        self.coloresorigen = self.colores
        self.textoorigen = self.text
        self.color = colores[0]

        self.botonOFF = False

    def dibujarBoton(self, cambiodepantalla):
        # Declaracion de variables globales. PantallaActual cambia segun el boton que se presione
        # y sonidoVolumen cambia entre True y False por cada click.

        # self.pos es una tupla que contiene las coordenadas actuales del cursor
        self.pos = pygame.mouse.get_pos()

        # Dibuja un rectangulo negro debajo del rectangulo del boton simulando un borde
        pygame.draw.rect(self.ventana, (0, 50, 0), (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        # Dibuja el rectangulo que se usara como boton
        pygame.draw.rect(self.ventana, self.color, (self.x, self.y, self.width, self.height), 0)

        # Si el texto tiene algun caracter, se dibuja dentro del boton usando una fuente contenida dentro de la carpeta
        if self.text != '':
            font = pygame.font.Font('VCR_OSD_MONO_1.001.ttf', self.tamletra)
            text = font.render(self.text, 1, (0, 0, 0))
            self.ventana.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

        # Si se presiona dentro del area del boton, el color cambia al tercer elemento de la lista colores
        if getEventoMouse() == "MOUSEBUTTONDOWN" and self.isOver(self.pos):
            if self.isOver(self.pos):
                self.color = self.colores[2]

        if self.permitireventos:
            # Se cumple la condicion si se suelta el click dentro del area del boton
            if getEventoMouse() == "MOUSEBUTTONUP" and self.isOver(self.pos):
                # Si el valor del parametro cambiodepantalla al llamar el metodo es "sonido", si la variable
                # "sonidoVolumen" de sonidos.py es False, se convierte en True y viceversa
                if cambiodepantalla == "sonido":
                    if not getSonidoVolumen():
                        setSonidoVolumen(True)
                    else:
                        setSonidoVolumen(False)
                # Si cambiodepantalla es "musica", entonces si el volumen de la musica reproducida es 0, se convierte en 0.5
                # y viceversa
                elif cambiodepantalla == "musica":
                    if pygame.mixer.music.get_volume() == 0:
                        pygame.mixer.music.set_volume(0.2)
                    else:
                        pygame.mixer.music.set_volume(0)
                # Si cambiodepantalla tiene cualquier otro valor (ya sea "nivel1", "menuprincipal", "menuamenazas", etc)
                # entonces pantallaActual cambia a ese valor
                else:
                    setPantallaActual(cambiodepantalla)

                # Si el boton Sonido esta en ON, se reproduce un sonido de Click al apretar el boton
                if getSonidoVolumen():
                    sonidoClick.play()

                # Si se llamo al parametro opcional coloresOFF, entonces si el boton esta en su estado OFF, al soltar el
                # click el color del boton y el texto va a corresponder a self.coloresOFF y self.textoOFF. Si esta en su
                # estado ON, al soltar el boton el texto va a ser self.text y el color self.colores
                if self.coloresOFF:
                    if self.botonOFF:
                        self.text = self.textoorigen
                        self.colores = self.coloresorigen
                        self.botonOFF = False
                    else:
                        self.text = self.textoOFF
                        self.colores = self.coloresOFF
                        self.botonOFF = True

                # Al soltar el boton, el color vuelve al color normal
                self.color = self.colores[0]

        # Si se mueve el mouse por encima del boton, el color se convierte en el primero de la lista de colores
        if getEventoMouse() == "MOUSEMOTION":
            # Hover al boton
            if self.isOver(self.pos):
                self.color = self.colores[1]
            else:
                self.color = self.colores[0]

    def isOver(self, pos):
        # Pos es la posicion del mouse en forma de tupla (x, y)
        # Si el mouse esta dentro del boton, devuelve True. En caso contrario, False
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False

    def setPermitirEventos(self):
        self.permitireventos = True
        self.colores = coloresazules


# Botones (tamano de letra, x, y, width, height, texto, colores, colores secundarios (opcional), texto secundario (
# opcional)) Los parametros secundarios son usados para los botones de sonido y musica que cambian de color y texto
# segun si son ON u OFF
botonjugar = Boton(True, 40, 480, 220, 170, 80, 'Jugar', coloresazules)
botoninstrucciones = Boton(True, 40, 370, 320, 370, 100, 'Instrucciones', coloresazules)
botonamenazas = Boton(True, 40, 370, 440, 370, 100, 'Amenazas', coloresazules)
botonmusica = Boton(True, 15, 900, 590, 100, 40, 'Musica ON', coloresverdes, coloresrojos, "Musica OFF")
botonsonido = Boton(True, 15, 1020, 590, 100, 40, 'Sonido ON', coloresverdes, coloresrojos, "Sonido OFF")
botonvolver = Boton(True, 15, 20, 590, 100, 40, 'Volver', coloresazules)
botonreintentar = Boton(True, 15, 140, 590, 100, 40, 'Reintentar', coloresazules)
botonsiguientenivel = Boton(True, 15, 900, 520, 220, 50, "Siguiente Nivel", coloresazules)
