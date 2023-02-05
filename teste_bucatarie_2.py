from test_bucatarie import TestBucatarie
from ingredient import Ingredient

class TestBucatarie2(TestBucatarie):

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