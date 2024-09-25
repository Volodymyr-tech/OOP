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
        else:
            raise TypeError("Продукт должен быть экземпляром класса Product")


    @property
    def products(self):
        """Список товаров в виде строк"""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str
