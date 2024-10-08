class PrintMixin:

    def __repr__(self):
        return f"{self.__class__.__name__}, {self.description}, {self.price}, {self.quantity}"
