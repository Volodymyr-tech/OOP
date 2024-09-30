from src.reader_json import object_json


# Тестовая функция с pytest
def test_object_json():
    # Фейковые данные JSON
    json_data = [
        {
            "name": "Electronics",
            "description": "Various electronic gadgets",
            "products": [
                {"name": "Phone", "price": 699, "quantity": 10, "description": "Smartphone"},
                {"name": "Laptop", "price": 1299, "quantity": 5, "description": "High-end laptop"},
            ],
        },
        {
            "name": "Groceries",
            "description": "Fresh food and groceries",
            "products": [
                {"name": "Apple", "price": 1, "quantity": 100, "description": "Fresh apple"},
                {"name": "Milk", "price": 2, "quantity": 50, "description": "Organic milk"},
            ],
        },
    ]

    # Вызов функции object_json
    categories = object_json(json_data)

    # Проверка: количество категорий
    assert len(categories) == 2

    # Проверка первой категории
    assert categories[0].name == "Electronics"
    assert categories[0].description == "Various electronic gadgets"
    assert categories[0].products_list[0].name == "Phone"
    assert categories[0].products_list[0].price == 699
    assert categories[0].products_list[0].quantity == 10

    # Проверка второй категории
    assert categories[1].name == "Groceries"
    assert categories[1].description == "Fresh food and groceries"
    assert categories[1].products_list[0].name == "Apple"
    assert categories[1].products_list[0].price == 1
    assert categories[1].products_list[0].quantity == 100
