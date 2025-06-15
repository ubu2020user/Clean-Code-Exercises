class Customer:
    def __init__(self, last_name, first_name):
        self._last_name = last_name
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    def __str__(self):
        return f"Customer(last_name='{self.last_name}', first_name='{self.first_name}')"