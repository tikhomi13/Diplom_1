from data import StellarBurgersTestData


class TestIngredient:

    def test_get_price(self):

        test_price = StellarBurgersTestData.ingredient_1.get_price()

        assert test_price == 44

    def test_get_name(self):

        test_name = StellarBurgersTestData.ingredient_1.get_name()

        assert test_name == 'Ingredient_1'

    def test_get_type(self):

        test_type = StellarBurgersTestData.ingredient_1.get_type()

        assert test_type == "SAUCE"
