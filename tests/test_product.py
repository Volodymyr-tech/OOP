from src.product import Product


def test_products(products):
    assert products.name == "Xiaomi Redmi Note 11"
    assert products.description == "1024GB, Синий"
    assert products.quantity == 14


def test_new_product(product_dict):
    new_product = Product.new_product(product_dict)
    assert new_product.name == "IPHONE 16"
    assert new_product.description == "1024GB, КРАСНЫЙ"
    assert new_product.quantity == 100


def test_product_price(products):
    assert products.price == 31000.0
    products.price = 40000
    assert products.price == 40000


def test_product_price_zero(products, capsys):
    products.price = -500
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_str(products):
    result = Product("IPHONE 16", "1024GB, КРАСНЫЙ", 1500000.0, 100)
    assert str(result) == "IPHONE 16, 1500000.0 руб. Остаток: 100 шт.\n"


def test_add(capsys):
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product1 + product2 == 2580000.0


def test_product_repr(capsys):
    # Создаем объект класса Product
    product = Product("Телефон", "Смартфон", 1000, 10)

    # Захватываем вывод в консоль
    print(repr(product))
    captured = capsys.readouterr()

    # Проверяем, что вывод соответствует ожидаемому
    assert captured.out == "Product, Смартфон, 1000, 10\n"
