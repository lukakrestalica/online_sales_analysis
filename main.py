from product import Product
from product_manager import ProductManager


def main():
    manager = ProductManager()
    manager.add_product(Product("Laptop", "800.00", 5))
    manager.add_product(Product("Mis", "20.00", 10))
    manager.add_product(Product("Tastatura", "45.00", 8))
    manager.add_product(Product("Monitor", "180.00", 4))

    manager.display_products()
    manager.display_total_value()


if __name__ == "__main__":
    main()
