from ingredient import Ingredient


class Reteta:
    def __init__(self, nume, portii):
        self.nume = nume
        self.portii = portii

        self.lista_ingrediente = []

    def adauga_ingredient(self, nume, cantitate, tip_cantitate):
        obiect_ingredient = Ingredient(nume, cantitate, tip_cantitate)
        self.lista_ingrediente.append(obiect_ingredient)

    def __str__(self):
        return f"{self.nume}: {self.lista_ingrediente}"
