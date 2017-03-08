class ListaFuerzas:
    # lista = []
    fuerza = 0, 0

    def add(self, fuerza):
        # self.lista.append(fuerza)
        self.fuerza= self.fuerza[0] + fuerza[0], self.fuerza[1] + fuerza[1]
        print(fuerza)

    def getFuerza(self):
        # suma = 0, 0
        # for fuerza in self.lista:
        #     suma = suma[0] + fuerza[0], suma[1] + fuerza[1]
        # return suma
        return self.fuerza

    def vacia(self):
        # self.lista = []
        self.fuerza = 0, 0
        print("se borra")
