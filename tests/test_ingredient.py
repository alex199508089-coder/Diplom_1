import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize('name', [
        'Секретный ингредиент',
        'Соус №12',
        'Начинка №9',
    ])
    def test_ingredient_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 1234)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('price', [
        100000,
        1234,
        12,
    ])
    def test_ingredient_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус №12', price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type', [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING,
    ])
    def test_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'Соус №12', 1234)
        assert ingredient.get_type() == ingredient_type
