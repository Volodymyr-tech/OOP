import pytest

from src.class_lawngrass import LawnGrass
from src.class_smartphone import Smartphone


def test_smartphone():
    smartphone = Smartphone(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 10, 2024, 1024, "red"
    )
    assert smartphone.name == "Samsung Galaxy C23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 10
    assert smartphone.model == 2024
    assert smartphone.memory == 1024
    assert smartphone.color == "red"


def test_add_smart():
    smartphone_1 = Smartphone(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 1, 5, 10, 2024, 1024, "red"
    )
    smartphone_2 = Smartphone("C23 Ultra", "256GB, 200MP камера", 1, 5, 100, 2025, 1000, "Серый цвет")

    result = smartphone_2 + smartphone_1

    assert result == 10


def test_add_raise_error():
    smartphone_1 = Smartphone(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 1, 5, 10, 2024, 1024, "red"
    )
    grass = LawnGrass(
        "Футбольный газон", "мелкие семена для посыпа поля весной", 10, 100000, "England", "1 week", "green"
    )

    with pytest.raises(TypeError):
        smartphone_1 + grass
