import os
import json
from src.classes import Category, Product

def reader_json(path: str) -> dict:
    '''Функция для чтения JSON файла'''
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def object_json(json_file: dict):
    """Функция создания объектов класса из данных json"""
    product_objects = []
    category_objects = []
    for category in json_file:
        category_objects.append(Category(**category))
        for product in category.get("products", []):
            product_objects.append(Product(**product))
    return category_objects, product_objects


if __name__ == '__main__':
    data = reader_json(r'..\data\products.json')

    res = object_json(data)

