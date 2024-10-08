from src.class_exception import ZeroQuantityError
from src.product import Product
from src.base_order import BaseOrderProduct


class Order(BaseOrderProduct):
    """Класс "заказ", информация о купленном товаре,
    кол-во а так же стоимость"""

    product: Product
    quantity: int

    order_id = 0

    def __init__(self, product, quantity):
        self.__product = product

        if quantity > 0:
            self.__quantity = quantity  # Колличество продукта
            print(f'{self.__product.name } добавлен')
        else:
            raise ZeroQuantityError

        self.order_id += 1
        Order.order_id += 1


    def __str__(self):
        return f"{self.__product.name}, {self.__product.description} {self.total_price()}"

    def total_price(self):
        total_price = self.__product.__quantity * self.__product.price
        return total_price


