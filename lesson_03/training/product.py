class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def prod_name(self):
        return self.name

    def prod_price(self):
        return self.price

    def name_price(self):
        return f"Наименование: {self.name}, цена: {self.price}."
