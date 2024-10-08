class ZeroQuantityError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Ваш список товаров пуст, так нельзя'

    def __str__(self):
        return self.message

