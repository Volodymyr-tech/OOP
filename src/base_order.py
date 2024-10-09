from abc import ABC, abstractmethod


class BaseOrderProduct(ABC):
    """Базовый класс краткой информации о товаре"""

    @abstractmethod
    def __str__(self):
        pass
