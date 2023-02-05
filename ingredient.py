class Ingredient:
    def __init__(self, nume, cantitate, tip_cantitate):
        self.nume = nume
        self.cantitate = cantitate
        self.tip_cantitate = tip_cantitate.lower()
        self.transformare_cant()

    def transformare_cant(self):
        if self.tip_cantitate == 'kg':
            self.tip_cantitate = 'gr'
        if self.tip_cantitate == 'l':
            self.tip_cantitate = 'ml'
        self.cantitate = self.cantitate * 1000
