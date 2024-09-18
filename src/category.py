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
        """Метод для добавления новых продуктов"""
        if isinstance(product, Product):
            for prod in self.__products:
                if prod.name == product.name:
                    Category.products_quantity += 1
                if prod.product_price < product.product_price:
                    prod.product_price = product.product_price
                    return
        else:
            raise TypeError("Продукт должен быть экземпляром класса Product")
        self.__products.append(product)
        Category.products_quantity += 1

    @property
    def products(self):
        """Список товаров в виде строк"""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.product_price} руб. Остаток: {product.quantity} шт.\n"
        return product_str
