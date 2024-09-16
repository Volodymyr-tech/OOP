from src.category import Category


def test_category(category_instance):
    assert category_instance.name == "Смартфоны"
    assert (
        category_instance.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert Category.products_quantity == 3
    assert Category.categories_quantity == 1

