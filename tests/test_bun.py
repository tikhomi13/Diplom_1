from praktikum.bun import Bun

class TestBun:

    def test_get_bun_name_name_returned(self):

        bun_1 = Bun(name='Булка', price=11)
        name = bun_1.get_name()

        assert name == 'Булка'

    def test_get_buns_price_price_returned(self):

        bun_1 = Bun(name='Булка', price=11)
        price = bun_1.get_price()

        assert price == 11

