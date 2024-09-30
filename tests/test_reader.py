import json
from unittest.mock import mock_open, patch

from src.reader_json import reader_json


def test_reader_json():
    # Подделываем содержимое JSON-файла
    mock_json_data = '[{"name": "Alice"}, {"name": "Bob"}]'  # JSON STRING

    # Замокаем open() и заставим его вернуть mock_json_data
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        # Замокаем также json.load, чтобы он правильно разобрал mock_json_data
        with patch("json.load", return_value=json.loads(mock_json_data)):
            result = reader_json("dummy_path.json")  # передаём фиктивный путь

            # Ожидаемый результат, который должен вернуть reader_json
            expected_result = [{"name": "Alice"}, {"name": "Bob"}]

            # Проверяем, что результат функции соответствует ожиданиям
            assert result == expected_result
