from abc import ABC, abstractmethod


class BaseOrderProduct(ABC):
    """Базовый класс краткой информации о товаре"""

    @abstractmethod
    def products(self):
        pass
