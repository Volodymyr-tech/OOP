from src.category import Category


class IterCategory:

    def __init__(self, category):

        if isinstance(category, Category):
            self.category = category
            self.current_value = 0

    def __iter__(self):
        self.current_value = 0
        return self

    def __next__(self):
        if self.current_value < len(self.category.products_list):
            product = self.category.products_list[self.current_value]
            self.current_value += 1
            return product
        else:
            raise StopIteration
