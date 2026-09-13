import pytest

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredientTypes:
    @pytest.mark.parametrize("constant, expected_value", [
        (INGREDIENT_TYPE_SAUCE, 'SAUCE'),
        (INGREDIENT_TYPE_FILLING, 'FILLING'),
    ])
    def test_ingredient_type_constant(self, constant, expected_value):
        assert constant == expected_value