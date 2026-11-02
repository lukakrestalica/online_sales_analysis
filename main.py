from product import Product
from product_manager import ProductManager


def main():
    manager = ProductManager()
    manager.add_product(Product("Laptop Pro", "800.00", 6))
    manager.add_product(Product("Bezicni mis", "20.00", 12))
    manager.add_product(Product("Tastatura", "45.00", 8))
    manager.add_product(Product("Monitor", "180.00", 4))



if __name__ == "__main__":
    main()
