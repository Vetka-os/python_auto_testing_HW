class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def prodName(self):
        return self.name

    def prodPrice(self):
        return self.price

    def NamePrice(self):
        return f"Наименование: {self.name}, цена: {self.price}."
