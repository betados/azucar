class ListaGranos:
    lista = []

    def add(self, grano):
        self.lista.append(grano)

    def dibuja(self):
        for grano in self.lista:
            grano.dibuja()

    def actualiza(self, t):
        for grano in self.lista:
            grano.actualiza(t)

    def getLista(self):
        return self.lista
