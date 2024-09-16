import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_instance():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации,"
        " но и получение дополнительных функций для удобства жизни",
        products=[
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
            {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
            {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
        ],
    )


@pytest.fixture
def products():
    return Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=14)
