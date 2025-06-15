from decimal import Decimal


class ShoppingItem:
    def __init__(self, name, price):
        self._name = name
        self._price = Decimal(price)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = Decimal(value)

    def __str__(self):
        return f"ShoppingItem(name='{self.name}', price={self.price})"
