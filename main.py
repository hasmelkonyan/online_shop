from user import User
from product import Product
from shopping_cart import ShoppingCart
from werehouse import Werehouse
import werehouse


if __name__ == '__main__':
    prod = Product("Phone", "iPhone 1500", 2010)
    wer = Werehouse(prod)
    wer.add_to_werehouse(5)
    print(werehouse.werehouse_dct)
    anna = User("Anna", "anna@gmail.com", 1)
    anna.get_shopping_cart().add_to_shopping_cart(prod)
    print(werehouse.werehouse_dct)


