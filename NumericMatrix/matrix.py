from __future__ import annotations
from typing import Union
import itertools
from copy import deepcopy
import math
from .exceptions import Exceptions
from fractions import Fraction
import operator
from functools import reduce


class NumericMatrix(object):

    def __init__(self, array: list):
        self.__cache = {}
        self.array = [*array]
        self.rows = [*array]
        self.columns = self.__get_cols()

    def __getitem__(self, float_):
        row, col = str(float_).split('.')
        return self.array[int(row) - 1][int(col) - 1]

    def __setitem__(self, float_, value):
        row, col = str(float_).split('.')
        self.array[int(row) - 1][int(col) - 1] = value

    '''
        For permutation of the row on cols
    '''
    def __get_cols(self) -> list:
        arr = deepcopy(self.rows)
        new_ar = [[] for i in range(0, len(self.rows[0]))]
        for column in new_ar:
            for row in arr:
                column.append(row.pop(0))
        return new_ar

    '''
        Use for floating index
    '''
    def __float(self, a, b):
        return float(str(f'{a}.{b}'))

    '''
        Check for equal cols and rows
        for __add__ and __sub__
    '''
    def check_rc(self, other: NumericMatrix) -> None:
        if len(self.rows) != len(other.rows):
            raise Exceptions.NotEqualRows
        elif len(self.columns) != len(other.columns):
            raise Exceptions.NotEqualColumns

    '''
        Check equal cols -> rows
        for __mul__ and __truediv__
    '''
    def check_mt(self, other: NumericMatrix) -> None:
        if len(self.columns) != len(other.rows):
            raise Exceptions.NotEqualColumns

    def __pow__(self, power, modulo=None):
        return reduce(operator.mul, [self for i in range(0, power)])

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.array))

    '''
        Addition for Matrix
    '''
    def __add__(self, other: NumericMatrix) -> NumericMatrix:
        self.check_rc(other)
        return NumericMatrix([[x + y for x, y in zip(selfRow, otherRow)]
                              for selfRow, otherRow in zip(self.rows, other.rows)])

    '''
        Subtraction for Matrix
    '''
    def __sub__(self, other: NumericMatrix) -> NumericMatrix:
        self.check_rc(other)
        return NumericMatrix([[x - y for x, y in zip(selfRow, otherRow)]
                              for selfRow, otherRow in zip(self.rows, other.rows)])

    '''
        Multiplication for Matrix and numbers
    '''
    def __mul__(self, other: Union[NumericMatrix, int, float]) -> NumericMatrix:

        if type(other) in [int, float]:
            return NumericMatrix([[x * other for x in row] for row in self.rows])

        self.check_mt(other)
        return NumericMatrix([
            [sum([x * y for x, y in [*itertools.zip_longest(selfRow, otherColumn)]]) for otherColumn in other.columns]
            for selfRow in self.rows])

    '''
        Division for Matrix and numbers
    '''
    def __truediv__(self, other: Union[NumericMatrix, int, float]) -> NumericMatrix:

        if type(other) in [int, float]:
            return NumericMatrix([[x / other for x in row] for row in self.rows])

        self.check_mt(other)
        return self * other.invert()

    '''
        Invert current matrix
    '''
    def invert(self):
        tr = self.transpone()
        return NumericMatrix([
            [tr.algebraic(rowCord, colCord) for colCord in range(1, len(row) + 1)]
            for rowCord, row in zip(range(1, len(tr.rows) + 1), tr.rows)
        ]) / self.determinant

    '''
        Same as __get_cols ,but return new object
    '''
    def transpone(self):
        return NumericMatrix(self.columns)

    def __eq__(self, other: NumericMatrix):
        return hash(other) == hash(self)

    '''
        Determinant of current matrix
    '''
    @property
    def determinant(self) -> Union[int, float]:
        if len(self.rows) != len(self.columns):
            raise Exceptions.NoDeterminant

        cached = self.__cache.get('determinant', None)
        if cached:
            return cached

        if len(self.rows) * len(self.columns) == 4:
            res = (self[1.1] * self[2.2]) - (self[1.2] * self[2.1])
            self.__cache['determinant'] = res
            return res

        elif len(self.rows) * len(self.columns) == 1:
            return self[1.1]

        res = sum([*map(lambda item: item[0] * (-1) ** item[1],
                        [(self[self.__float(rowCord, 1)] * self.minore(rowCord, 1), rowCord + 1)
                         for rowCord in range(1, len(self.rows) + 1)])
                   ])
        self.__cache['determinant'] = res
        return res

    '''
        Same as minore, but multiplication (-1) in power col + row
    '''
    def algebraic(self, rowCord: int, colCord: int) -> Union[int, float]:
        return int(math.pow(-1, (rowCord + colCord))) * self.minore(rowCord, colCord)

    '''
        Find a minore of
        current row and column current for matrix
    '''
    def minore(self, rowCord: int, colCord: int) -> Union[int, float]:
        rows = deepcopy(self.rows)
        rows.pop(rowCord - 1)
        return NumericMatrix([row for row in rows if row.pop(colCord - 1) + math.inf]).determinant

    def __repr__(self):

        def _re(number):
            if isinstance(number, float):
                return str(Fraction(number).limit_denominator())
            return str(number)

        return '\n\t' + '\n\t'.join([repr([_re(x) for x in row]) for row in self.rows])
