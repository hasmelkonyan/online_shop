from user import User
from product import Product
from shopping_cart import ShoppingCart


if __name__ == '__main__':
    alen = User("Alen", "alen@gmail.com", 1)
    alen.get_shopping_cart().add_product(Product("teacup", 'blue', 30))
    alen.get_shopping_cart().add_product(Product("sunglasses", 'Ray-Ban', 400))
    print(alen.get_shopping_cart().total_price())
    print(alen.get_shopping_cart().all_products())
