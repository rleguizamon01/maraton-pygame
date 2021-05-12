import pygame
from configuracion import ventana


class RectanguloCursor(object):
    # Dibuja un rectangulo con texto que sigue el movimiento del cursor
    def __init__(self, tamletra, width, height, posarribaizquierda, posabajoderecha, imagen, text1=None, text2=None,
                 text3=None, text4=None):
        # Solicita un tamano de letra, el ancho del rectangulo, el alto, el comienzo del area de la imagen sobre la
        # que se va a usar, el fin, la imagen, y cuatro textos opcionales para escribir dentro del rectangulo
        self.tamletra = tamletra
        self.width = width
        self.height = height
        self.posarribaizquierda = posarribaizquierda
        self.posabajoderecha = posabajoderecha
        self.imagen = imagen
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.text4 = text4

        self.pos = pygame.mouse.get_pos()
        self.canttexto = 0

    def cursoralrededor(self):
        # Si el cursor esta dentro del area de la imagen, devuelve True
        if self.posabajoderecha[0] > self.pos[0] and self.pos[0] > self.posarribaizquierda[0]:
            if self.posabajoderecha[1] > self.pos[1] and self.pos[1] > self.posarribaizquierda[1]:
                return True
        return False

    def dibujarrectangulo(self):
        # Dibuja un rectangulo que cambia su altura segun la cantidad de parametros opcionales de texto llamados
        self.pos = pygame.mouse.get_pos()

        if self.text1:
            self.canttexto = 40
            if self.text2:
                self.canttexto = 70
                if self.text3:
                    self.canttexto = 100
                    if self.text4:
                        self.canttexto = 130

        self.imagen = pygame.transform.scale(self.imagen, (self.width, self.canttexto))

        # Si el cursor esta dentro del area de la imagen, dibuja el texto dentro del rectangulo
        if self.cursoralrededor():
            ventana.blit(self.imagen, (self.pos[0], self.pos[1]))

            # Si el texto tiene algun caracter y es llamado en el objeto, se dibuja
            if self.text1 != '' and self.text1:
                font = pygame.font.Font('VCR_OSD_MONO_1.001.ttf', self.tamletra)
                text = font.render(self.text1, 1, (0, 0, 0))
                ventana.blit(text, (self.pos[0] + 10, self.pos[1] + 10))

                if self.text2 != '' and self.text2:
                    font = pygame.font.Font('VCR_OSD_MONO_1.001.ttf', self.tamletra)
                    text = font.render(self.text2, 1, (0, 0, 0))
                    ventana.blit(text, (self.pos[0] + 10, self.pos[1] + 40))

                    if self.text3 != '' and self.text3:
                        font = pygame.font.Font('VCR_OSD_MONO_1.001.ttf', self.tamletra)
                        text = font.render(self.text3, 1, (0, 0, 0))
                        ventana.blit(text, (self.pos[0] + 10, self.pos[1] + 70))

                        if self.text4 != '' and self.text4:
                            font = pygame.font.Font('VCR_OSD_MONO_1.001.ttf', self.tamletra)
                            text = font.render(self.text4, 1, (0, 0, 0))
                            ventana.blit(text, (self.pos[0] + 10, self.pos[1] + 100))
