from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class StellarBurgersTestData:

    bun_1 = Bun(name='Булка', price=11)
    ingredient_1 = Ingredient(ingredient_type='SAUCE', name='Ingredient_1', price=44)
    ingredient_2 = Ingredient(ingredient_type='SAUCE', name='Ingredient_2', price=43)
    list_of_ingredients = [["SAUCE", 'test_sauce', 5]]


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
