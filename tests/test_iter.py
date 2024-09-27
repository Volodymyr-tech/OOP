import pytest

from src.class_iter import IterCategory


def test_iter(category_):
    iter_start = IterCategory(category_)
    assert str(next(iter_start)) == "Iphone 15, 95000 руб. Остаток: 8 шт.\n"
    assert str(next(iter_start)) == "Iphone 16pro, 150000 руб. Остаток: 16 шт.\n"

    with pytest.raises(StopIteration):
        next(iter_start)
