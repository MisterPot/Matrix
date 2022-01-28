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

    class ZeroMinore(Exception):
        def __str__(self):
            return "Minore index can't equal 0"

    class NoDeterminant(Exception):
        def __str__(self):
            return "This matrix can't have determinant"
