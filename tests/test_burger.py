from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from data import StellarBurgersTestData


class TestBurger:

    def test_set_buns_bun_set(self):

        StellarBurgersTestData.bun_1.get_name()

        burger_1 = Burger()
        burger_1.set_buns(StellarBurgersTestData.bun_1)

        bun_name = burger_1.bun.get_name()
        bun_price = burger_1.bun.get_price()

        assert bun_name == 'Булка' and bun_price == 11

    def test_add_ingredient(self):

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
        burger_1.set_buns(StellarBurgersTestData.bun_1)
        price = burger_1.bun.get_price()

        assert price == 11

    def test_get_receipt(self):

        burger_1 = Burger()
        burger_1.set_buns(StellarBurgersTestData.bun_1)
        expected_result = (
            f'(==== Булка ====)\n'
            f'(==== Булка ====)\n'
            f'\nPrice: 22'
        )

        assert burger_1.get_receipt() == expected_result
