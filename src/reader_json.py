import json
import os

from src.category import Category
from src.product import Product


def reader_json(path: str) -> list:
    """Функция для чтения JSON файла"""
    # full_path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def object_json(json_file: list):
    """Функция создания объектов класса из данных json"""
    category_objects = []

    for category_data in json_file:

        products_list = [Product(**product_data) for product_data in category_data.get("products", [])]
        category = Category(name=category_data['name'],
                            description=category_data['description'],
                            products=products_list)

        category_objects.append(category)
    return category_objects


if __name__ == "__main__":

    # Формируем путь к файлу относительно рабочей директории
    file_path = os.path.join("data", "products.json")
    data = reader_json(file_path)
    res = object_json(data)
    print(res)
