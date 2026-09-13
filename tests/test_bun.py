import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('price', [
        0,
        1234,
        12345678,
    ])
    def test_bun_price(self, price):
        bun = Bun('test_name', price)
        assert bun.get_price() == price

    @pytest.mark.parametrize('name', [
        '',
        'test name',
        '8734 queiu 1298_%',
    ])
    def test_bun_name(self, name):
        bun = Bun(name, 1234)
        assert bun.get_name() == name