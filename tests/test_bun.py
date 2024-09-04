from data import StellarBurgersTestData


class TestBun:

    def test_get_bun_name_name_returned(self):

        name = StellarBurgersTestData.bun_1
        actual_result = name.get_name()
        assert actual_result == 'Булка'

    def test_get_buns_price_price_returned(self):

        price = StellarBurgersTestData.bun_1
        actual_result = price.get_price()
        assert actual_result == 11
