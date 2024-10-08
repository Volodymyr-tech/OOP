import pytest

from src.class_exception import ZeroQuantityError
from src.product import Product
from src.order import Order

def setup_function():
    Order.order_id = 0


def test_order():
    product1 = Product("Programs", "goodbyedpi", "free", quantity=200)
    product2 = Product("Developer", "backend", 4000, quantity=1)

    order_1 = Order(product1, 2)
    order_2 = Order(product2, 2)
    order_3 = Order(product2, 2)
    order_4 = Order(product2, 2)

    assert order_1.order_id == 1
    assert order_2.order_id == 2
    assert order_3.order_id == 3
    assert order_4.order_id == 4
    assert Order.order_id == 4


def test_raise_error_capsys(capsys):
    product1 = Product("Programs", "goodbyedpi", 150, quantity=10)
    with pytest.raises(ZeroQuantityError):
        order = Order(product1, 0)

        captured = capsys.readouterr()
        assert captured.out == 'Ваш список товаров пуст, так нельзя\n'



def test_capsys(capsys):
    product1 = Product("Programs", "goodbyedpi", 1500, quantity=10)
    order = Order(product1, 1)
    captured = capsys.readouterr()
    assert captured.out == 'Programs добавлен\n'
    assert order._product.quantity == 9


def test_product_quantity():
    product1 = Product("Programs", "goodbyedpi", 1500, quantity=10)
    order = Order(product1, 5)
    assert order._product.quantity == 5


def test_str():
    product1 = Product("Programs", "goodbyedpi", 1500, quantity=10)
    order = Order(product1, 5)

    assert str(order) == "Programs, goodbyedpi 7500"