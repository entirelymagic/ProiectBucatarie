import bucatarie
from ingredient import Ingredient
from bucatarie import Bucatarie
from unittest import TestCase
from reteta import Reteta
from unittest.mock import MagicMock, patch
from produs_finit import ProdusFinit


class TestBucatarie(TestCase):
    def setUp(self):
        self.zahar = Ingredient("zahar", 2000, "gr")
        self.bucatarie1 = Bucatarie("Bucatarie 1")
        self.faina = Ingredient("faina", 5, "kg")

    def test_ingredient(self):
        assert self.faina.nume == "faina"
        assert self.faina.tip_cantitate == "gr"
        assert self.faina.cantitate == 5000

    def test_adaugare_ingredient_in_bucatarie(self):
        self.bucatarie1.adauga_ingrediente(self.faina)
        self.bucatarie1.adauga_ingrediente(self.zahar)
        lista_nume_ingrediente = [i.nume for i in self.bucatarie1.inventar]
        assert self.faina.nume in lista_nume_ingrediente
        assert self.zahar.nume in lista_nume_ingrediente

    def test_adaugare_acelasi_ingredient(self):
        cantitate_dubla_faina = self.faina.cantitate * 2
        self.bucatarie1.adauga_ingrediente(self.faina)
        for ingredient_inventar in self.bucatarie1.inventar:
            if ingredient_inventar.nume == self.faina.nume:
                assert ingredient_inventar.cantitate == self.faina.cantitate

        self.bucatarie1.adauga_ingrediente(self.faina)
        for ingredient_inventar in self.bucatarie1.inventar:
            if ingredient_inventar.nume == self.faina.nume:
                assert ingredient_inventar.cantitate == cantitate_dubla_faina

    def test_verificare_cand_disponibila_inventar(self):
        reteta = Reteta("Mamaliga cu branza", 8)
        reteta.adauga_ingredient("malai", 500, 'gr')
        reteta.adauga_ingredient("apa", 750, 'ml')
        reteta.adauga_ingredient("sare", 50, "gr")

        # Acestea sunt ingredientele pe care le vom adauga in bucatarie

        malai = Ingredient("malai", 1000, 'gr')
        apa = Ingredient("apa", 2000, 'ml')
        sare = Ingredient("sare", 500, "gr")

        self.bucatarie1.adauga_ingrediente(malai)
        self.bucatarie1.adauga_ingrediente(apa)
        self.bucatarie1.adauga_ingrediente(sare)

        assert self.bucatarie1.verifica_cant_disponibila_inventar(reteta) is True

    def test_verificare_cand_nu_avem_disponibil_in_inventar(self):
        reteta = Reteta("Mamaliga cu branza", 5)
        reteta.adauga_ingredient("malai", 500, 'gr')
        reteta.adauga_ingredient("apa", 750, 'ml')
        reteta.adauga_ingredient("sare", 50, "gr")

        # Acestea sunt ingredientele pe care le vom adauga in bucatarie

        malai = Ingredient("malai", 200, 'gr')
        apa = Ingredient("apa", 2000, 'ml')
        sare = Ingredient("sare", 500, "gr")

        self.bucatarie1.adauga_ingrediente(malai)
        self.bucatarie1.adauga_ingrediente(apa)
        self.bucatarie1.adauga_ingrediente(sare)

        assert self.bucatarie1.verifica_cant_disponibila_inventar(reteta) is False

    def test_preparare_reteta(self):
        reteta_mamaliga = Reteta("Mamaliga cu branza", 8)
        reteta_mamaliga.adauga_ingredient("malai", 500, 'gr')
        reteta_mamaliga.adauga_ingredient("apa", 750, 'ml')
        reteta_mamaliga.adauga_ingredient("sare", 50, "gr")


        malai = Ingredient("malai", 1000, 'gr')
        apa = Ingredient("apa", 2000, 'ml')
        sare = Ingredient("sare", 500, "gr")

        self.bucatarie1.adauga_ingrediente(malai)
        self.bucatarie1.adauga_ingrediente(apa)
        self.bucatarie1.adauga_ingrediente(sare)
        # Am creat un produs finit
        produs_finit = ProdusFinit(reteta_mamaliga.nume, reteta_mamaliga.portii)
        # creem un obiect de tip mock care sa ne returneze un produs finit
        mock = MagicMock(return_value=produs_finit)
        # Cu patch am inlocuit ce ne returneaza metoda prepara cu rezultatul din mock
        with patch('bucatarie.Bucatarie.prepara', mock):
            # Am verificat ca ceea ce ne returneaza metoda prepara este egal cu produsul finit creat
            assert self.bucatarie1.prepara(reteta_mamaliga) == produs_finit

    def test_preparare_reteta_fara_ingrediente_necesare(self):
        reteta_mamaliga = Reteta("Mamaliga cu branza", 8)
        reteta_mamaliga.adauga_ingredient("malai", 500, 'gr')
        reteta_mamaliga.adauga_ingredient("apa", 750, 'ml')
        reteta_mamaliga.adauga_ingredient("sare", 50, "gr")

        malai = Ingredient("malai", 1000, 'gr')
        sare = Ingredient("sare", 500, "gr")

        self.bucatarie1.adauga_ingrediente(malai)
        self.bucatarie1.adauga_ingrediente(sare)

        assert self.bucatarie1.prepara(reteta_mamaliga) is False

    def test_preparare_reteta1(self):
        reteta_mamaliga = Reteta("Mamaliga cu branza", 8)
        reteta_mamaliga.adauga_ingredient("malai", 500, 'gr')
        reteta_mamaliga.adauga_ingredient("apa", 750, 'ml')
        reteta_mamaliga.adauga_ingredient("sare", 50, "gr")
        malai = Ingredient("malai", 1000, 'gr')
        apa = Ingredient("apa", 2000, 'ml')
        sare = Ingredient("sare", 500, "gr")

        self.bucatarie1.adauga_ingrediente(malai)
        self.bucatarie1.adauga_ingrediente(apa)
        self.bucatarie1.adauga_ingrediente(sare)

        rez = self.bucatarie1.prepara(reteta_mamaliga)

        assert isinstance(rez, ProdusFinit)
