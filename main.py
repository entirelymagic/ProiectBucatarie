from ingredient import Ingredient
from bucatarie import Bucatarie
from reteta import Reteta

ingredient1 = Ingredient("faina", 5, "Kg")
ingredient2 = Ingredient("sare", 1000, "gr")
ingredient3 = Ingredient("apa", 10, "l")

bucatarie1 = Bucatarie("Bucatarie 1")

bucatarie1.adauga_ingrediente(ingredient1)
bucatarie1.adauga_ingrediente(ingredient2)
bucatarie1.adauga_ingrediente(ingredient3)

bucatarie1.salvare()

# reteta1 = Reteta("Paine")

# print(reteta1.nume)
