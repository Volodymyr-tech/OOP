from src.class_smartphone import Smartphone


def test_smartphone():
    smartphone = Smartphone("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 10,2024,1024,'red')
    assert smartphone.name == "Samsung Galaxy C23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 10
    assert smartphone.model == 2024
    assert smartphone.memory == 1024
    assert smartphone.color == 'red'