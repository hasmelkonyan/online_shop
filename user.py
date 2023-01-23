from shopping_cart import ShoppingCart


class User:
    def __init__(self, name, email, user_id):
        self.__name = name
        self.__email = email
        self.__user_id = user_id
        self.__shopping_cart = ShoppingCart()

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_user_id(self):
        return self.__user_id

    def get_shopping_cart(self):
        return self.__shopping_cart



