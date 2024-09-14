
def test_category(category):
    assert category.name == 'Смартфоны'
    assert category.description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert category.products_quantity == 3
    assert category.categories_quantity == 1


def test_products(products):
    assert products.name == 'Xiaomi Redmi Note 11'
    assert products.description == '1024GB, Синий'
    assert products.quantity == 14




