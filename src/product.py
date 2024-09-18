class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name                                    # Имя продукта
        self.description = description                      # Описание продукта
        self.price = price                                  # Цена продукта
        self.quantity = quantity                            # Колличество продукта


    @classmethod
    def new_product(cls, product_dict):
        '''Метод для получения объекта Product через словарь'''
        return cls(**product_dict)