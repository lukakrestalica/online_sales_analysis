"""Korpa sadrzi odvojene Product objekte sa kupljenim kolicinama."""
from decimal import Decimal
from product import Product


class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product, quantity=1):
        if not isinstance(product, Product):
            raise TypeError("Ocekivan je Product objekat.")
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Kolicina u korpi mora biti pozitivan ceo broj.")
        existing = next((p for p in self.cart_items
                         if p.name.casefold() == product.name.casefold()), None)
        combined = quantity + (existing.quantity if existing else 0)
        if combined > product.quantity:
            raise ValueError("Nema dovoljno proizvoda na stanju.")
        if existing:
            existing.update_quantity(combined)
        else:
            self.cart_items.append(Product(product.name, product.price, quantity))

    def total_value(self):
        return sum((p.price * p.quantity for p in self.cart_items), Decimal("0.00"))

    def display_contents(self):
        if not self.cart_items:
            print("Korpa je prazna.")
        for product in self.cart_items:
            product.display_info()
