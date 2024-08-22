from praktikum.bun import Bun
from data import StellarBurgersTestData
class TestBun:

    def test_get_bun_name_name_returned(self):

        name = StellarBurgersTestData.bun_1.get_name()
        assert name == 'Булка'

    def test_get_buns_price_price_returned(self):

        price = StellarBurgersTestData.bun_1.get_price()
        assert price == 11
