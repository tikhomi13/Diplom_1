class Bun:
    """
    Модель булочки для бургера.
    Булочке можно дать название и назначить цену.
    """

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price


bun_1 = Bun(name='Булка', price=11)
print(bun_1.get_name())
print(bun_1.get_price())



