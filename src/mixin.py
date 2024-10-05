from abc import ABC, abstractmethod


class PrintMixin(ABC):

    def __repr__(self):
        print(f'{self.__class__.__name__}, {self.description}, {self.price}, {self.quantity}')
