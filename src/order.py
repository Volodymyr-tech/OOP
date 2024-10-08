from src.product import Product
from src.base_order import BaseOrderProduct


class Order(BaseOrderProduct):
    """Класс "заказ", информация о купленном товаре,
    кол-во а так же стоимость"""

    product: Product
    quantity: int

    order_id = 0

    def __init__(self, product, quantity):
        self.__products = product
        self.__quantity = quantity
        self.__total_price = 0
        self.order_id += 1

        Order.order_id += 1

    @property
    def products(self):
        return f"{self.__products.name}, {self.__products.description}"

    @property
    def quantity(self):
        return self.__quantity

    @products.setter
    def products(self, new_product):
        raise ValueError("Добавлять новый товар в уже созданный заказ невозможно!")

    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity += new_quantity

    @property
    def total_price(self):
        self.__total_price = self.__quantity * self.__products.price
        return self.__total_price
