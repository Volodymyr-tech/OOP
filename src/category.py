from src.product import Product

class Category:
    name: str
    description: str
    products: list

    categories_quantity = 0
    products_quantity = 0

    def __init__(self, name, description, products):
        self.name = name  # имя категории
        self.description = description  # Описание категории
        self.__products = products  # Список продуктов

        Category.categories_quantity += 1  # колличество категорий
        Category.products_quantity += len(self.__products)  # колличество продуктов

    def __str__(self):
        total_quantity = 0
        for item in self.__products:
            total_quantity += item.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

    def add_product(self, product):
        """Метод для добавления нового продукта или обновления существующего"""
        if isinstance(product, Product):
            # Проверяем, есть ли продукт с таким же именем
            for existing_product in self.__products:
                if existing_product.name == product.name:
                    # Обновляем количество и цену, если продукт уже есть
                    existing_product.quantity += product.quantity
                    existing_product.price = max(existing_product.price, product.price)
                    return
            self.__products.append(product)
            Category.products_quantity = len(self.__products)
        else:
            raise TypeError("Продукт должен быть экземпляром класса Product")

    @property
    def products(self):
        """Список товаров в виде строк"""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    @property
    def products_list(self):
        return self.__products

    def average_price(self):
        '''Метод подсчитывает средний ценник всех товаров.'''
        try:
            # Если товаров нет, то деление на 0 вызовет исключение
            if len(self.__products) == 0:
                raise ZeroDivisionError("Нет товаров в категории")

            total_price = sum([product.price for product in self.__products])
            return total_price / len(self.__products)

        except ZeroDivisionError:
            print("Ошибка: В категории нет товаров, невозможно вычислить среднюю цену.")
            return 0
