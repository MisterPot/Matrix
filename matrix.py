from fractions import Fraction
from copy import deepcopy
from ls import list


class Exceptions:
    class NotEqualRows(Exception):
        def __str__(self):
            return 'Not equal count of rows with other matrix'

    class NotEqualColumns(Exception):
        def __str__(self):
            return 'Not equal columns of rows with other matrix'

    class NotAdded(Exception):
        def __str__(self):
            return "Can't add the matrix or number to this matrix"


class Matrix(object):

    def __init__(self, array: list):
        self.array = deepcopy(array)
        self.__transform()
        self.rows = len(array)
        self.columns = len(array[0])

    def __setattr__(self, key, value):
        self.__set(key, value)
        if 'columns' in self.__dict__:
            self.__refresh()

    def __set(self, key, value):
        object.__setattr__(self, key, value)

    def __refresh(self):
        self.__set('rows', len(self.array))
        self.__set('columns', len(self.array[0]))

    def __transform(self):
        self.__set('array', list(self.array))
        for row in self.array:
            self.array.replace(row, list(row))

    def transpone(self):
        transponed = self.__ls(self.columns)
        in_array = deepcopy(self.array)
        for column in transponed:
            for row in in_array:
                column.append(row.pop(0))

        self.array = transponed

    def __ls(self, count):
        ls = list()
        for i in range(0, count):
            ls.append(list())
        return ls

    # Додавання
    def __add__(self, array_or_number):
        def number(number_):
            for row in self.array:
                for num in row:
                    row.replace(num, num + number_, from_end=True)

        def matrix(matrix_: Matrix):
            if self.rows != matrix_.rows:
                raise Exceptions.NotEqualRows

            if self.columns != matrix_.columns:
                raise Exceptions.NotEqualColumns

            else:
                ls1 = deepcopy(self.array)
                ls2 = deepcopy(matrix_.array)
                result = self.__ls(self.rows)

                for row1, row2, res_row in zip(ls1, ls2, result):
                    for number1, number2 in zip(row1, row2):
                        res_row.append(number1 + number2)

                self.array = result

        funcs = {Matrix: matrix,
                 int: number,
                 float: number}
        funcs[type(array_or_number)](array_or_number)

    # Віднімання
    def __sub__(self, array_or_number):
        def number(number_):
            for row in self.array:
                for num in row:
                    row.replace(num, num - number_, from_end=True)

        def matrix(matrix_):
            if self.rows != matrix_.rows:
                raise Exceptions.NotEqualRows

            if self.columns != matrix_.columns:
                raise Exceptions.NotEqualColumns

            else:
                ls1 = deepcopy(self.array)
                ls2 = deepcopy(matrix_.array)
                result = self.__ls(self.rows)

                for row1, row2, res_row in zip(ls1, ls2, result):
                    for number1, number2 in zip(row1, row2):
                        res_row.append(number1 - number2)

                return Matrix(result)

        funcs = {Matrix: matrix,
                 int: number,
                 float: number}
        funcs[type(array_or_number)](array_or_number)

    def __mul__(self, array_or_number):
        def number(number_):
            for row in self.array:
                for num in row:
                    row.replace(num, num * number_, from_end=True)

        def matrix(matrix_):

            if self.rows == matrix_.columns:
                matrix_.transpone()
                new_matrix = self.__ls(self.rows)
                # new_mat
            else:
                raise Exception

        funcs = {Matrix: matrix,
                 int: number,
                 float: number}
        funcs[type(array_or_number)](array_or_number)

    def __truediv__(self, array_or_number):
        def number(number_):
            for row in self.array:
                for num in row:
                    row.replace(num, num / number_, from_end=True)

        def matrix(matrix_):
            print(matrix_)

        funcs = {Matrix: matrix,
                 int: number,
                 float: number}
        funcs[type(array_or_number)](array_or_number)

    def __repr__(self):

        arr = deepcopy(self.array)
        for row in arr:
            for num in row:
                if isinstance(num, float):
                    el = Fraction(num).limit_denominator().__str__()
                    row.replace(num, el)
                else:
                    continue

        f = ''
        for row in arr:
            f += f'\n{row.__repr__()}'
        f += '\n'
        return f
