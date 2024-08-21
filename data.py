from unittest.mock import Mock
from unittest.mock import patch
from burger import Burger
from bun import Bun
from ingredient import Ingredient


class MockBun:

    bun_mock = Mock(spec=Bun)
    bun_mock.get_price.return_value = 300.0

    mocked_burger = Burger()
    mocked_burger.bun = bun_mock


class MockIngredient:

    ingredient_mock = Mock(spec=Ingredient)
    ingredient_mock.get_price.return_value = 200.0

    mocked_burger = Burger()
    mocked_burger.ingredients = [ingredient_mock]




