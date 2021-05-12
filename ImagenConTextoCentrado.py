import pygame
from configuracion import ventana


class ImagenConTextoCentrado(object):
    # Dibuja una imagen con un texto centrado debajo
    def __init__(self, imagen, x, y, texto, tamletra, width, height):
        # Los parametros solicitan la direccion de una imagen, la posicion en x e y, el texto a mostrar
        # debajo, el tamano de la letra del texto, el ancho de la imagen y su altura

        self.imagen = imagen
        self.x = x
        self.y = y
        self.texto = texto
        self.tamletra = tamletra
        self.width = width
        self.height = height

    def dibujarimagenn(self):
        # Escala la imagen segun la altura y el ancho determinado

        self.imagen = pygame.transform.scale(self.imagen, (self.width, self.height))

        # Dibuja el texto centrado
        fuente = pygame.font.Font('VCR_OSD_MONO_1.001.ttf', self.tamletra)
        texto = fuente.render(self.texto, 1, (0, 0, 0))
        ventana.blit(self.imagen, (self.x, self.y))
        
        ventana.blit(texto, (self.x + (self.width / 2 - texto.get_width() / 2), self.y + self.height/2 - texto.get_height() / 2))

        

    def getposarribaizquierdaa(self):
        # Devuelve la posicion inicial de la imagen
        return self.x, self.y

    def getposabajoderechaa(self):
        # Devuelve la posicion final de la imagen
        return self.x + self.width, self.y + self.height
