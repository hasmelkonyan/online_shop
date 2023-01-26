from product import Product
import werehouse


class ShoppingCart:
    def __init__(self):
        self.__products = []

    def add_to_shopping_cart(self, product):
        if isinstance(product, Product):
            self.__products.append(product.get_product_name())
            werehouse.werehouse_dct[product.get_product_name()] -= 1

    def remove_from_shopping_cart(self, product):
        if isinstance(product, Product) and product in self.__products:
            self.__products.remove(product.get_product_name())
            werehouse.werehouse_dct[product.get_product_name()] += 1

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

