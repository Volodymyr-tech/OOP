


class Product():
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity ):
        self.name = name
        self. description = description
        self.price = price
        self.quantity = quantity




class Category():
    name: str
    description: str
    products: list

    categories_quantity = 0
    products_quantity = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.categories_quantity += 1
        Category.products_quantity += len(self.products)



