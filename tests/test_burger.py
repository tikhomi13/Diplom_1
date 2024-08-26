from unittest.mock import Mock


from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from data import StellarBurgersTestData




class TestBurger:

    def test_set_buns_bun_set(self):

           # убрать в переменные
        StellarBurgersTestData.bun_1.get_name()

        burger_1 = Burger()
        burger_1.set_buns(StellarBurgersTestData.bun_1)
        assert burger_1.bun.get_name() == 'Булка' and burger_1.bun.get_price() == 11

    def test_add_ingredient(self):   # рабочие вызовы методов . Пробую сделать мок

        StellarBurgersTestData.bun_1.get_name()

        burger_1 = Burger()
        burger_1.set_buns(StellarBurgersTestData.bun_1)

        ingredient = Ingredient(ingredient_type='SAUCE', name='Ingredient_1', price=44)
        burger_1.add_ingredient(ingredient)
        assert len(burger_1.ingredients) == 1

    def test_remove_ingredient(self):

        burger_1 = Burger()
        burger_1.add_ingredient(StellarBurgersTestData.ingredient_1)
        burger_1.add_ingredient(StellarBurgersTestData.ingredient_2)
        burger_1.remove_ingredient(0)

        assert len(burger_1.ingredients) == 2
        assert len(burger_1.ingredients) == 1

    def test_move_ingredient(self):

        burger_1 = Burger()
        burger_1.add_ingredient(StellarBurgersTestData.ingredient_1)
        burger_1.add_ingredient(StellarBurgersTestData.ingredient_2)
        burger_1.move_ingredient(1, 0)
        assert burger_1.ingredients[0] == StellarBurgersTestData.ingredient_2

    def test_get_price(self):

        StellarBurgersTestData.bun_1.get_name()
        StellarBurgersTestData.bun_1.get_price()

        burger_1 = Burger()
        burger_1.set_buns(StellarBurgersTestData.bun_1)    # этого не хватало
        assert burger_1.bun.get_price() == 11

    def test_get_receipt(self):

        burger_1 = Burger()
        burger_1.set_buns(StellarBurgersTestData.bun_1)
        expected_result = (
            f'(==== Булка ====)\n'
            f'(==== Булка ====)\n'
            f'\nPrice: 22'
        )

        assert burger_1.get_receipt() == expected_result

    def test_bun_mock(self):   # РАБОЧИЙ МОК

        bun_mock = Mock(spec=Bun)
        ingredient_mock = Mock(spec=Ingredient)

        bun_mock.get_price.return_value = 300.0
        ingredient_mock.get_price.return_value = 200.0

        mocked_burger = Burger()
        mocked_burger.bun = bun_mock
        mocked_burger.ingredients = [ingredient_mock]

        assert mocked_burger.get_price() == 800.0
