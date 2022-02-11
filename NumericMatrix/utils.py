import random


def use_mode(displayMode=True):
    def f(func):
        def args_(self, *args, **kwargs):
            if self.displayMode is displayMode:
                raise AttributeError('This function disabled')
            return func(self, *args, **kwargs)
        return args_
    return f


def generate_matrix(rows, cols, num_range=(-10, 10)):
    return [[random.randint(*num_range) for x in range(0, cols)] for row in range(0, rows)]
