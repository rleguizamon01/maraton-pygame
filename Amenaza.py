import pygame


# Enemigo
class Amenaza(object):
    def __init__(self, xamenaza, yamenaza):
        # Solicita la posicion inicial de la amenaza mediante xamenaza e yamenaza
        self.xamenaza = xamenaza
        self.yamenaza = yamenaza

        # Las amenazas comienzan con 3 corazones
        self.corazones = 3

        # Las amenazas comienzan estando lejos de la Zona Segura
        self.amenazaEnZona = False

        # Cantidad limite de casillas que se mueve hacia un lado al estar viva
        self.limitemovimiento = 2
        self.estaBajando = True
        self.direccion = "VERTICAL"

    def impactoDisparo(self, xydisparo):
        if xydisparo == (self.xamenaza, self.yamenaza) and self.corazones > 0:
            self.corazones -= 1

    def moverAmenaza(self, movimientojugador, xydisparo):

        self.impactoDisparo(xydisparo)
        # El parametro movimientojugador puede tener 3 posibles valores, y el tercero es una tupla (es decir,
        # es un (x, y) que se puede dividir) la lista entera se podria leer como: movimientojugador = [0, 1, [2.1,
        # 2.2]] (los num son la posicion dentro de la lista) movimientojugador[0] = xjugador movimientojugador[1] =
        # yjugador movimientojugador[2] = lado hacia el que se movio (tupla) (x,y) movimientojugador[2][0] = sentido
        # x en que se movio el jugador (1 = derecha, -1 = izquierda) movimientojugador[2][1] = sentido y en que se
        # movio el jugador (1 = abajo, -1 = arriba)

        # Si la amenaza todavia no fue llevada a la Zona Segura, se ejecutan las siguientes condiciones
        if not self.amenazaEnZona:
            if self.corazones > 0:
                # Se ejecuta lo siguiente solo si la amenaza continua con vida
                    # self.estaBajando es True cuando esta moviendose aumentando en y y en False cuando su movimiento
                    # disminuye en y. A self.limitemovimiento se le reduce desde 3 a 0 con paso -0.25 cada vez para que
                    # al llegar a un numero entero se mueva. De esta manera se crea un temporizador para la amenaza tarde
                    # un poco mas en moverse.
                if self.direccion == "VERTICAL":
                    if self.estaBajando:
                        self.limitemovimiento -= 0.25
                        if self.limitemovimiento == int(self.limitemovimiento):
                            self.yamenaza += 1
                            if self.limitemovimiento == 0:
                                self.estaBajando = False
                    # Hace lo mismo que la condicion anterior pero para subir.
                    else:
                        self.limitemovimiento += 0.25
                        if self.limitemovimiento == int(self.limitemovimiento):
                            self.yamenaza -= 1
                            if self.limitemovimiento == 2:
                                self.estaBajando = True

                elif self.direccion == "HORIZONTAL":
                    if self.estaBajando:
                        self.limitemovimiento -= 0.25
                        if self.limitemovimiento == int(self.limitemovimiento):
                            self.xamenaza += 1
                            if self.limitemovimiento == 0:
                                self.estaBajando = False
                    # Hace lo mismo que la condicion anterior pero para subir.
                    else:
                        self.limitemovimiento += 0.25
                        if self.limitemovimiento == int(self.limitemovimiento):
                            self.xamenaza -= 1
                            if self.limitemovimiento == 2:
                                self.estaBajando = True

            if movimientojugador[0] == (self.xamenaza, self.yamenaza) and self.corazones == 0:
                # Si el jugador esta en la misma posicion que la amenaza, mover la amenaza
                self.xamenaza += movimientojugador[1][0]
                self.yamenaza += movimientojugador[1][1]
        else:
            # Si la amenaza fue llevada a la zona segura, se transporta a la coordenada (0, 0)
            self.xamenaza = 0
            self.yamenaza = 0

    def comprobarRehacer(self, boolean, ladomovimiento, xyamenaza):
        if boolean and xyamenaza == (self.xamenaza, self.yamenaza):
            self.xamenaza += ladomovimiento[0] * -1
            self.yamenaza += ladomovimiento[1] * -1

    def setAmenazaEnZona(self, amenazaEnZona):
        # Permite cambiar el valor de self.amenazaEnZona desde fuera de la clase
        self.amenazaEnZona = amenazaEnZona

    def setCantCorazones(self, cantCorazones):
        # Permite cambiar la cantidad de corazones desde fuera de la clase
        self.corazones = cantCorazones

    def getxycorazonesamenaza(self):
        # Devuelve la posicion de la amenaza
        return (self.xamenaza, self.yamenaza), self.corazones

    def setDireccionMovimiento(self, direccionmovimiento):
        self.direccion = direccionmovimiento


def getXyAmenazas(amenaza1, amenaza2=None, amenaza3=None, amenaza4=None, amenaza5=None):
    listaxyamenazas = [amenaza1]
    if amenaza2:
        listaxyamenazas.append(amenaza2)
    if amenaza3:
        listaxyamenazas.append(amenaza3)
    if amenaza4:
        listaxyamenazas.append(amenaza4)
    if amenaza5:
        listaxyamenazas.append(amenaza5)
    return listaxyamenazas
