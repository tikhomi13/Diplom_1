import pytest
from unittest.mock import Mock
from burger import Burger
from bun import Bun

from ingredient import Ingredient
from typing import List
from unittest.mock import patch
from praktikum import Database

my_ingredients = [["SAUCE", 'test_sauce', 5]]


class TestBurger:

    def test_set_buns_bun_set(self):

        bun_1 = Bun(name='Булка', price=11)    # убрать в переменные
        bun_1.get_name()

        burger_1 = Burger()
        burger_1.set_buns(bun_1)   # None так как set_buns устанавливает значение, а не возвращает

        burger_1.bun.get_name()
        burger_1.bun.get_price()

        print(burger_1.bun.get_name())    # тут вместо bun может быть мок
        print(burger_1.bun.get_price())

        assert burger_1.bun.get_name() == 'Булка'
        assert burger_1.bun.get_price()


    def test_add_ingredient(self):   # рабочие вызовы методов . Пробую сделать мок

        bun_1 = Bun(name='Булка', price=11)
        bun_1.get_name()

        burger_1 = Burger()
        burger_1.set_buns(bun_1)

        ingredient = Ingredient(ingredient_type='SAUCE', name='Ingredient_1', price=44)

        burger_1.add_ingredient(ingredient)

        # ДОДЕЛАТЬ

    #    print(burger.get_price())
       # print(burger.get_receipt())

    def test_remove_ingredient(self):

        pass


    def test_move_ingredient(self):

        pass

    def test_get_price(self):

        pass

    def test_get_receipt(self):

        pass





    def test_kame_mock(self):   # РАБОЧИЙ МОК

        bun_mock = Mock(spec=Bun)
        ingredient_mock = Mock(spec=Ingredient)

        bun_mock.get_price.return_value = 300.0
        ingredient_mock.get_price.return_value = 200.0

        mocked_burger = Burger()
        mocked_burger.bun = bun_mock
        mocked_burger.ingredients = [ingredient_mock]

        assert mocked_burger.get_price() == 800.0





        database = Database()

        burger_0 = Burger()

        test_buns = database.available_buns()
        print(test_buns)

        test_ingredients = database.available_ingredients()
        print(test_ingredients)

        burger_0.set_buns(test_buns[0])

        burger_0.add_ingredient(test_ingredients[1])
        burger_0.add_ingredient(test_ingredients[4])
        burger_0.add_ingredient(test_ingredients[3])
        burger_0.add_ingredient(test_ingredients[5])

        burger_0.move_ingredient(2, 1)

        burger_0.remove_ingredient(3)

        print(burger_0.get_price())
        print(burger_0.get_receipt())




       #burger_1,ingredient.add_ingredient(ingredient)

      #  print(burger_1.ingredients)


     #   get_list_of_ingredients = burger_1.ingredients

    def test_get_ingredients(self):

        burger = Burger()
        burger.ingredients

        print(burger.ingredients) # - Получаем список.

    #@patch('data.MockBun.mock_bun', return_value=MockBun)
    def test_set_buns_with_mock(self, mock_bun):




        pass

