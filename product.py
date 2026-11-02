"""Model proizvoda; cene su izrazene u EUR."""
from decimal import Decimal, InvalidOperation


class Product:
    def __init__(self, name, price, quantity):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Naziv proizvoda ne sme biti prazan.")
        self.name = name.strip()
        try:
            amount = Decimal(str(price))
        except InvalidOperation as exc:
            raise ValueError("Cena mora biti broj.") from exc
        if not amount.is_finite() or amount < 0:
            raise ValueError("Cena mora biti konacan nenegativan broj.")
        self.price = amount.quantize(Decimal("0.01"))
        self.update_quantity(quantity)

    def update_quantity(self, quantity):
        """Postavlja novu kolicinu, ne povecava je za dati iznos."""
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Kolicina mora biti nenegativan ceo broj.")
        self.quantity = quantity

    def display_info(self):
        print(f"{self.name}: {self.price:.2f} EUR x {self.quantity} = "
              f"{self.price * self.quantity:.2f} EUR")
