import random
from cart import Cart
from product import Product
from product_manager import ProductManager


def main():
    manager = ProductManager()
    manager.add_product(Product("Laptop Pro", "800.00", 6))
    manager.add_product(Product("Bezicni mis", "20.00", 12))
    manager.add_product(Product("Tastatura", "45.00", 8))
    manager.add_product(Product("Monitor", "180.00", 4))


    cart = Cart()
    available = [p for p in manager.products if p.quantity > 0]
    for product in random.sample(available, 3):
        cart.add_product(product)
    print("Sadrzaj korpe (po jedan komad tri nasumicna proizvoda):")
    cart.display_contents()
    print(f"Ukupno za naplatu: {cart.total_value():.2f} EUR")



if __name__ == "__main__":
    main()
