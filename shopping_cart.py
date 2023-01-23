from product import Product


class ShoppingCart:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)

    def remove_product(self, product):
        if isinstance(product, Product) and product in self.__products:
            self.__products.remove(product)

    def total_price(self):
        total = 0
        for product in self.__products:
            total += product.get_price()
        return total

    def all_products(self):
        all = []
        for product in self.__products:
            all.append((product.get_product_name(), product.get_price()))
        return all
