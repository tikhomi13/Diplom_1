from praktikum.ingredient import Ingredient

class TestIngredient:

    def test_get_price(self):

        ingr_1 = Ingredient(ingredient_type='SAUCE', name='Ingredient_1', price=44)
        assert ingr_1.get_price() == 44

    def test_get_name(self):

        ingr_1 = Ingredient(ingredient_type='SAUCE', name='Ingredient_1', price=44)
        assert ingr_1.get_price() == 44

    def test_get_type(self):

        ingr_1 = Ingredient(ingredient_type='SAUCE', name='Ingredient_1', price=44)
        assert ingr_1.get_type() == "SAUCE"


