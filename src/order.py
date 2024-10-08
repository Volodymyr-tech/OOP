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
        self._product = product

        if quantity > 0:
            self._quantity = quantity  # Колличество продукта
            print(f'{self._product.name } добавлен')
        else:
            raise ZeroQuantityError

        self._product.quantity -= self._quantity

        Order.order_id += 1
        self.order_id = Order.order_id



    def __str__(self):
        return f"{self._product.name}, {self._product.description} {self.total_price()}"

    def total_price(self):
        total_price = self._quantity * self._product.price
        return total_price


