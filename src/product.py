from src.base_product import BaseProduct
from src.mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name  # Имя продукта
        self.description = description  # Описание продукта
        self.__price = price  # Цена продукта
        if quantity:
            self.quantity = quantity  # Колличество продукта
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__repr__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other):
        if type(self) is type(other):
            return (self.quantity * self.price) + (other.quantity * other.price)
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_dict):
        """Метод для получения объекта Product через словарь"""
        return cls(**product_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif price < self.__price:
            user = input("Вы уверены, что хотите понизить цену?\n" '"Y" - YES, "N" - NO ')
            if user == "Y":
                self.__price = price
                print(f"Цена была изменена на {price}")
            else:
                print(f"Цена осталась прежней ({self.__price})")
        else:
            self.__price = price
