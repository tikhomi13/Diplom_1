from typing import List

import bun
# from praktikum.bun import Bun
# from praktikum.ingredient import Ingredient
#from bun import bun_1


from bun import Bun
from ingredient import Ingredient


class Burger:
    """
    Модель бургера.
    Бургер состоит из булочек и ингредиентов (начинка или соус).
    Ингредиенты можно перемещать и удалять.
    Можно распечать чек с информацией о бургере.
    """

    def __init__(self):
        self.bun = None
        self.ingredients: List[Ingredient] = []

    def set_buns(self, bun: Bun):
        self.bun = bun

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index: int):
        del self.ingredients[index]

    def move_ingredient(self, index: int, new_index: int):
        self.ingredients.insert(new_index, self.ingredients.pop(index))

    def get_price(self) -> float:
        price = self.bun.get_price() * 2

        for ingredient in self.ingredients:
            price += ingredient.get_price()

        return price

    def get_receipt(self) -> str:
        receipt: List[str] = [f'(==== {self.bun.get_name()} ====)']

        for ingredient in self.ingredients:
            receipt.append(f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =')

        receipt.append(f'(==== {self.bun.get_name()} ====)\n')
        receipt.append(f'Price: {self.get_price()}')

        return '\n'.join(receipt)


bun_1 = Bun(name='Булка', price=11)
bun_1.get_name()


burger_1 = Burger()
print(burger_1.set_buns(bun_1))

print(burger_1.bun) ###

print(burger_1.bun.get_name())

print(burger_1.bun.get_price()) # !!!!!!!!!!!!!!! вот так

print(burger_1.ingredients)


#burger_1.ingredients.append(bun_1)

#print(burger_1.ingredients)

#print(burger_1.set_buns(Bun(name='ffffff', price=2)))


#print(burger_1.set_buns(Bun.bun_1))





