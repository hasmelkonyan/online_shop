from product import Product

werehouse_dct = {}


class Werehouse:
    def __init__(self, product):
        if isinstance(product, Product):
            self.__product = product

    def set_product(self, product):
        self.__product = product

    def get_product(self):
        return self.__product

    def add_to_werehouse(self, quan):
        werehouse_dct[self.__product.get_product_name()] = quan

    def remove_from_werehouse(self):
        if self.__product.get_product_name() in werehouse_dct:
            del werehouse_dct[self.__product]