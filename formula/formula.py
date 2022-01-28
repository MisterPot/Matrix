class Formula(object):

    def __init__(self, formula: str):
        self.formula = formula
        self.__func = self.__get_func()

    def __call__(self, *args, **kwargs):
        return self.__func(*args, **kwargs)

    def __get_func(self):
        if not 'f' in self.formula:
            raise KeyError('Key "f" not in formula')
        attrs, execution = self.formula.split(' = ')
        return eval(f"lambda {attrs.split('f')[1].split('(')[1].split(')')[0]}: {execution}")

    def __repr__(self):
        return self.formula
