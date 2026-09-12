from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_set_burger_bun(self):
        bun = Bun('Bun 1', 666)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_to_burger(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус №3', 777)
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_from_burger(self):

        ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        ingredients = burger.ingredients
        assert len(ingredients) == 0

    def test_move_ingredient_in_burger(self):
        first_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус №3', 777)
        second_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Начинка №3', 36)
        burger = Burger()
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [second_ingredient, first_ingredient]

    @pytest.mark.parametrize('ingredients', [
        [Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус №1', 35)],
        [Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус №1', 35),
         Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус №2', 50)],
    ])
    def test_get_burger_price(self, ingredients):
        bun = Bun('Bun 1', 666)
        burger = Burger()
        burger.set_buns(bun)
        target_price = bun.price * 2
        for ingredient in ingredients:
            target_price += ingredient.price
            burger.add_ingredient(ingredient)
        assert burger.get_price() == target_price

    def test_get_burger_receipt_without_ingredients(self):
        bun = Bun('Bun 1', 666)
        burger = Burger()
        burger.set_buns(bun)
        target_price = bun.price * 2
        target_receipt = [
            f'(==== {bun.name} ====)',
            f'(==== {bun.name} ====)',
            '',
            f'Price: {target_price}'
        ]
        target_receipt = "\n".join(target_receipt)
        assert burger.get_receipt() == target_receipt

    def test_get_burger_receipt_with_ingredient(self):
        bun = Bun('Bun 1', 666)
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус №3', 777)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        target_price = bun.price * 2 + ingredient.price
        target_receipt = [
            f'(==== {bun.name} ====)',
            f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =',
            f'(==== {bun.name} ====)',
            '',
            f'Price: {target_price}'
        ]
        target_receipt = "\n".join(target_receipt)
        assert burger.get_receipt() == target_receipt

    def test_get_burger_receipt_with_several_ingredients(self):
        bun = Bun('Bun 1', 666)
        first_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус №3', 777)
        second_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Начинка №3', 36)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        target_price = bun.price * 2 + first_ingredient.price + second_ingredient.price
        target_receipt = [
            f'(==== {bun.name} ====)',
            f'= {str(first_ingredient.get_type()).lower()} {first_ingredient.get_name()} =',
            f'= {str(second_ingredient.get_type()).lower()} {second_ingredient.get_name()} =',
            f'(==== {bun.name} ====)',
            '',
            f'Price: {target_price}'
        ]
        target_receipt = "\n".join(target_receipt)
        assert burger.get_receipt() == target_receipt