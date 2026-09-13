from .bun import Bun
from .ingredient import Ingredient
from .ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Database:
    def __init__(self):
        self.buns = []
        self.ingredients = []

        self.buns.append(Bun("black bun", 100))
        self.buns.append(Bun("white bun", 200))
        self.buns.append(Bun("red bun", 300))

        self.ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
        self.ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200))
        self.ingredients.append(Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300))

        self.ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100))
        self.ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200))
        self.ingredients.append(Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300))

    def available_buns(self):
        return self.buns

    def available_ingredients(self):
        return self.ingredients