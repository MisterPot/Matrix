# Matrix

Simple variation matrix in Python.
* Instalation
    
      git clone https://github.com/MisterPot/Matrix.git

## Initialize matrix
```python
from Matrix.NumericMatrix.matrix import NumericMatrix
mat = NumericMatrix([
  [1, 2],
  [3, 4],
  [5, 6]
])

mat2 = NumericMatrix([
  [6, 5],
  [4, 3],
])
```


## Mathematical operations with matrix

  Supported all simple mathematical operations related with numbers
  ( +, - , / , * ).

  When you are doing any operation with matrix, returned new Matrix object !
  ```python
  print(mat / 2)
  #
  #['1/2', '1']
  #['3/2', '2']
  #['5/2', '3']
  #
  print(mat * 2)
  #
  #['2', '4']
  #['6', '8']
  #['10', '12']
  #
  print(mat * mat2)
  #
  #['14', '11']
  #['34', '27']
  #['54', '43']
  #
  print(mat / mat2)
  #
  #['5/2', '-7/2']
  #['7/2', '-9/2']
  #['9/2', '-11/2']
  #
  print(mat2**2)
  #
  #['56', '45']
  #['36', '29']
  #
  ```

## Matrix methods

  | Method | Args | What its do |
  |:-----------:|:-------:|:--------:|
  |`NumericMatrix.transpone`| `self` | just transpone matrix |
  

  ```python
  print(mat.transpone())
  #
  #['1', '3', '5']
  #['2', '4', '6']
  #
  ```

  | Method | Args | What its do |
  |:-----------:|:-------:|:--------:|
  |`NumericMatrix.__getitem__`| `float` | may get row, column and number |
  |`NumericMatrix.__setitem__`| `float` | replace existing number|

  ```python
  print(mat[1.1])
  #1
  print(mat[0.1])
  #[1, 3, 5]
  print(mat[1.0])
  #[1, 2]
  mat[2.2] = 2
  print(mat)
  #
  #['1', '2']
  #['3', '2']
  #['5', '6']
  # 
  ```
  | Method | Args | What its do |
  |:-----------:|:-------:|:--------:|
  |`NumericMatrix.invert`| `self` | invert current matrix |
  ```python
  print(m2.invert())
  #
  #['-3/2', '5/2']
  #['2', '-3']
  #
```

  | Method | Args | What its do |
  |:-----------:|:-------:|:--------:|
  |`NumericMatrix.determinant`| `self` | get determinant of current matrix (if matrix square) |
  ```python
  print(mat2.determinant)
  #
  # -2
  #
  print(mat.determinant)
  #
  # Exception: NoDeterminant
  #
```
  | Method | Args | What its do |
  |:-----------:|:-------:|:--------:|
  |`NumericMatrix.minore`| `int,int` | get minore of current row and column this matrix |
  |`NumericMatrix.algebraic`|`int,int`| same as minore, but multiplicate to (-1)**(row + col)|
  ```python
  print(mat2.minore(1, 2))
  #
  # 4
  #
  print(mat2.algebraic(1, 2))
  #
  # -4
  #
```

## Utils to any mathematical formulas

  Module have utils as Formula, to simplify any mathematical operations
```python
from Matrix.formula.formula import Formula
from Matrix.NumericMatrix.matrix import NumericMatrix
f = Formula('f(x, b) = x**2 + b')
mat1 = NumericMatrix([
  [1, 1],
  [4, 2]
])
mat2 = NumericMatrix([
  [2, 1],
  [3, 2]
])
print(f(mat1, mat2))
#
#['7', '4']
#['15', '10']
#
```