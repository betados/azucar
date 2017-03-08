import pygame
import random
import math
from sumaFuerzas import ListaFuerzas

class Grano:
    pantalla=0
    color=0
    radio=20
    acel= [0.0, 0.0]
    vel = [0.0, 0.0]
    normal = [0.0, 0.0]
    g= 0.0, 0.0005
    k=0.01
    fuerza = 0.0 , 0.0
    aerodinamica=0.001

    sumaFuerzas = 0, 0


    def __init__(self,pantalla):
        self.pantalla=pantalla
        self.pos = pygame.mouse.get_pos()
        self.color =[random.randrange(255), random.randrange(255), random.randrange(255)]
        # self.masa = 8
        self.masa = math.pow(self.radio, 3)*0.001
        self.fuerzaG=self.g[0]*self.masa, self.g[1]*self.masa

    def actualiza(self, t):
        self.tiempo=t

        self.addFuerza(self.fuerzaG)
        self.addFuerza(self.getFuerzaAerodinamica())

        self.acel = self.sumaFuerzas[0]/self.masa,  self.sumaFuerzas[1]/self.masa
        self.vel = self.vel[0]+0.5*self.acel[0]*t*t, self.vel[1]+0.5*self.acel[1]*t*t
        self.pos = self.pos[0] + self.vel[0]*t, self.pos[1] + self.vel[1]*t

        # vacia la suma de fuerzas en cada iteracion
        self.sumaFuerzas = 0, 0

    def dibuja(self):
        pygame.draw.circle(self.pantalla, self.color, [int(self.pos[0]), int(self.pos[1])], self.radio)
        # print(self.pos)

    def getRadio(self):
        return self.radio

    def getPos(self):
        return self.pos

    def getVel(self):
        return self.vel

    def setFuerza(self, vector, superposicion):
        if superposicion<0:
            superposicion = superposicion * -1
        fuerzaElasica = self.k * superposicion * 0.9
        self.addFuerza( [fuerzaElasica * vector[0], fuerzaElasica * vector[1]])

    def getG(self):
        return self.g[1]

    def getMasa(self):
        return self.masa

    def setNormal(self, superposicion):
        fuerza = ((self.modulo(self.vel)*0.1*self.masa)/self.tiempo) + self.k * superposicion * 0.9
        self.addFuerza([0,  - fuerza - self.fuerzaG[1]])

    def modulo(self, vector):
        return math.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2))

    def addFuerza(self,fuerza):
        self.sumaFuerzas = self.sumaFuerzas[0]+fuerza[0], self.sumaFuerzas[1]+fuerza[1]

    def getFuerzaAerodinamica(self):
        # para que la fuerza aerodinamica siempre se opona a la velocidad
        if self.vel[0]>0:
            multX=-1
        else:
            multX=1
        if self.vel[1] > 0:
            multY = -1
        else:
            multY = 1
        return math.pow(self.vel[0], 2) * self.aerodinamica * multX,\
               math.pow(self.vel[1], 2) * self.aerodinamica * multY