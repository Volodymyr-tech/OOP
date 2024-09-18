import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_quantities():
    # Сбрасываем значения перед каждым тестом
    Category.products_quantity = 0
    Category.categories_quantity = 0


def test_category(category_instance):
    assert category_instance.name == "Смартфоны"
    assert (
        category_instance.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert Category.products_quantity == 3
    assert Category.categories_quantity == 1


def test_add_product():
    # Создаем объекты продуктов
    laptop = Product("Laptop", "High-performance laptop", 1200.00, 10)
    smartphone = Product("Smartphone", "Latest model smartphone", 800.00, 5)

    # Создаем объект категории с двумя продуктами
    category = Category("Electronics", "Gadgets and devices", [laptop, smartphone])
    assert Category.products_quantity == 2

    # Создаем новый продукт и добавляем его в категорию
    tablet = Product("Tablet", "Portable tablet", 600.00, 15)
    category.add_product(tablet)

    assert Category.products_quantity == 3

    smartwatch = Product("Smartwatch", "Wearable smartwatch", 250.00, 20)
    category.add_product(smartwatch)

    assert Category.products_quantity == 4


def test_products(category):
    expected_output = (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )
    assert category.products == expected_output
