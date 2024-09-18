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

