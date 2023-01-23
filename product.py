class Product:
    def __init__(self, product_name, description, price):
        self.__product_name = product_name
        self.__description = description
        self.__price = price

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def get_product_name(self):
        return self.__product_name

    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price
