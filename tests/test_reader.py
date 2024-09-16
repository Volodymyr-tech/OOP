from unittest.mock import patch

import pytest

from src.reader_json import reader_json


# @pytest.mark.parametrize(
#     "path_json, output_dict_json",
#     [
#         (
#             r"C:\Users\Владимир\PycharmProjects\OOP\data\products.json",
#             [
#                 {
#                     "name": "Смартфоны",
#                     "description": "Смартфоны, как средство не только коммуникации,"
#                     " но и получение дополнительных функций для удобства жизни",
#                     "products": [
#                         {
#                             "name": "Samsung Galaxy C23 Ultra",
#                             "description": "256GB, Серый цвет, 200MP камера",
#                             "price": 180000.0,
#                             "quantity": 5,
#                         },
#                         {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
#                         {
#                             "name": "Xiaomi Redmi Note 11",
#                             "description": "1024GB, Синий",
#                             "price": 31000.0,
#                             "quantity": 14,
#                         },
#                     ],
#                 },
#                 {
#                     "name": "Телевизоры",
#                     "description": "Современный телевизор,"
#                     " который позволяет наслаждаться просмотром, станет вашим другом и помощником",
#                     "products": [
#                         {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
#                     ],
#                 },
#             ],
#         )
#     ],
# )
# @patch("json.load")
# def test_reader_json(mock_data, path_json, output_dict_json):
#     mock_data.return_value = output_dict_json
#
#     result = reader_json(path_json)
#
#     assert result == output_dict_json
