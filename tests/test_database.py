import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_database_buns_count(self):
        database = Database()
        assert len(database.available_buns()) == 3

    @pytest.mark.parametrize("index, bun_name, bun_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300),
    ])
    def test_database_bun_name(self, index, bun_name, bun_price):
        database = Database()
        buns = database.available_buns()
        assert buns[index].name == bun_name

    @pytest.mark.parametrize("index, bun_name, bun_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300),
    ])
    def test_database_bun_price(self, index, bun_name, bun_price):
        database = Database()
        buns = database.available_buns()
        assert buns[index].price == bun_price

    def test_database_ingredients_count(self):
        database = Database()
        assert len(database.available_ingredients()) == 6

    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_database_ingredient_type(self, index, ingredient_type, ingredient_name, ingredient_price):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[index].type == ingredient_type

    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_database_ingredient_name(self, index, ingredient_type, ingredient_name, ingredient_price):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[index].name == ingredient_name

    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_database_ingredient_price(self, index, ingredient_type, ingredient_name, ingredient_price):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[index].price == ingredient_price
