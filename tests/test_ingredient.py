from data import StellarBurgersTestData


class TestIngredient:

    def test_get_price(self):

        assert StellarBurgersTestData.ingredient_1.get_price() == 44

    def test_get_name(self):

        assert StellarBurgersTestData.ingredient_1.get_name() == 'Ingredient_1'

    def test_get_type(self):

        assert StellarBurgersTestData.ingredient_1.get_type() == "SAUCE"
