"""Upravljanje listom dostupnih proizvoda."""
from decimal import Decimal
from product import Product


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Ocekivan je Product objekat.")
        if any(p.name.casefold() == product.name.casefold() for p in self.products):
            raise ValueError("Proizvod sa ovim nazivom vec postoji.")
        self.products.append(product)

    def display_products(self):
        if not self.products:
            print("Inventar je prazan.")
        for product in self.products:
            product.display_info()

    def total_value(self):
        return sum((p.price * p.quantity for p in self.products), Decimal("0.00"))

    def display_total_value(self):
        print(f"Ukupna vrednost inventara: {self.total_value():.2f} EUR")

    def remove_product(self, name):
        """Uklanja proizvod po nazivu; vraca True ako je pronadjen."""
        for product in self.products:
            if product.name.casefold() == name.strip().casefold():
                self.products.remove(product)
                return True
        return False
