class Store:
    def __init__(self, name):
        self.name = name
        self.product = []

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        pass