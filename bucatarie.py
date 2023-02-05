from ingredient import Ingredient
from reteta import Reteta
from produs_finit import ProdusFinit


class Bucatarie:
    def __init__(self, nume: str):
        self.nume: str = nume
        self.inventar: list = []

    def adauga_ingrediente(self, ingredient: Ingredient):
        # numar_ingrediente_inventar = []
        # for i in self.inventar:
        #     numar_ingrediente_inventar.append(i.nume)
        #
        nume_ingrediente_inventar = [i.nume for i in self.inventar]

        if ingredient.nume in nume_ingrediente_inventar:
            for ingredient_inventar in self.inventar:
                if ingredient.nume == ingredient_inventar.nume:
                    ingredient_inventar.cantitate += ingredient.cantitate
        else:
            self.inventar.append(ingredient)

    def verifica_cant_disponibila_inventar(self, reteta: Reteta):
        nume_ingrediente_inventar = [i.nume for i in self.inventar]
        for ingredient_reteta in reteta.lista_ingrediente:
            if ingredient_reteta.nume not in nume_ingrediente_inventar:
                return False
            for ingredient_inventar in self.inventar:
                if ingredient_reteta.nume == ingredient_inventar.nume:
                    if ingredient_reteta.cantitate >= ingredient_inventar.cantitate:
                        return False
        return True

    def salvare(self):
        lista_inventar = []
        for ingredient in self.inventar:
            lista_inventar.append([ingredient.nume, ingredient.cantitate, ingredient.tip_cantitate])

        # lista_inventar = [[ingredient.nume, ingredient.cantitate, ingredient.tip_cantitate] for ingredient in self.inventar]

        data = {'nume': self.nume, 'inventar': lista_inventar}
        with open('bucatarie.txt', 'w') as file:
            file.write(str(data))

    def prepara(self, reteta: Reteta):
        if self.verifica_cant_disponibila_inventar(reteta):
            for ingredient_reteta in reteta.lista_ingrediente:
                for ingredient_inventar in self.inventar:
                    if ingredient_reteta.nume == ingredient_inventar.nume:
                        ingredient_inventar.cantitate = ingredient_inventar.cantitate - ingredient_reteta.cantitate
            return ProdusFinit(reteta.nume, reteta.portii)
        else:
            return False
