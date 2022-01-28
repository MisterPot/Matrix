from . import NumericMatrix
import unittest


class TestMatrix(unittest.TestCase):

    def setUp(self) -> None:
        self.matrix1 = NumericMatrix([[1, 2], [3, 4]])
        self.matrix2 = NumericMatrix([[2, 3], [4, 1]])

    @unittest.skip
    def testTruedivMatrix(self):
        pass

    def testTruedivNumber(self):
        new = self.matrix1 / 2
        self.assertEqual(new, NumericMatrix([[0.5, 1], [1.5, 2]]))

    def testMulMatrix(self):
        new = self.matrix1 * self.matrix2
        self.assertEqual(new, NumericMatrix([[10, 5], [22, 13]]))

    def testMulNumber(self):
        new = self.matrix1 * 2
        self.assertEqual(new, NumericMatrix([[2, 4], [6, 8]]))


if __name__ == '__main__':
    unittest.main()