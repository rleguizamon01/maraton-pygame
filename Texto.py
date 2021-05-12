import pygame
from configuracion import ventana
from imagenes import rectangulogris

class Texto(object):
    # Dibuja un texto en una posicion especifica
    def __init__(self, x, y, texto, tamletra, color=None):
        # Solicita la posicion en x e y deltexto, el texto a mostrar, el tamano de la letra y, opcionalmente,
        # el color del texto

        self.x = x
        self.y = y
        self.texto = texto
        self.tamletra = tamletra
        self.color = color

    def dibujarTexto(self):
        # Dibuja el texto en la posicion determinada con el color asignado y, si no lo esta,
        # se toma por defecto el color negro
        fuente = pygame.font.Font('VCR_OSD_MONO_1.001.ttf', self.tamletra)
        if self.color:
            texto = fuente.render(self.texto, 1, self.color)
        else:
            texto = fuente.render(self.texto, 1, (0, 0, 0))
        ventana.blit(texto, (self.x, self.y))


def dibujarTitulo(texto):
    # Solicita un texto y lo dibuja centrado por encima de la ventana
    width, height = pygame.display.get_surface().get_size()

    fuente = pygame.font.Font('VCR_OSD_MONO_1.001.ttf', 50)
    text = fuente.render(texto, 1, (153, 204, 255))
    ventana.blit(text, (0 + (width / 2 - text.get_width() / 2), 20))


def textoVictoriaPasos(contadorPasos, cantmaxima):
    # Dibuja la cantidad de pasos realizados en la pantalla Victoria
    # contadorPasos[0] es un String con los pasos y el maximo y contadorPasos[1] es el numero de pasos
    if contadorPasos[1] <= cantmaxima:
        return "Hiciste solo " + contadorPasos[0] + " pasos! Segui asi!"
    else:
        return "Hiciste " + contadorPasos[0] + " pasos. Estuvo bien, pero podria ser mejor!"


def dibujarrectangulofondo(altura, y, ancho=None, x=None):
    # Dibuja un rectangulo usando una imagen de la carpeta con una determinada altura y posicion en y
    imagen = rectangulogris
    if ancho:
        imagen = pygame.transform.scale(imagen, (ancho, altura))
    else:
        imagen = pygame.transform.scale(imagen, (900, altura))
    if x:
        ventana.blit(imagen, (x, y))
    else:
        ventana.blit(imagen, (120, y))