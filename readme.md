# Matrix

Simple variation matrix in Python.
* Instalation
    
      git clone https://github.com/MisterPot/Matrix.git


* Simple usage

  ```python
  from matrix import Matrix
  
  q = [
    [1,2],
    [3,4],
    [5,6]
    ]
  
  mat = Matrix(q)
  
  print(mat + 1)   
  #
  #[2,3]
  #[4,5]
  #[6,7]
  # 
  ```

##Other mathematical operations with matrix

  Supported all simple mathematical operations related with numbers
  ( +, - , / , * ).

  When you are doing any operation with matrix, returned new Matrix object !

  
  
  ```python
  print(mat - 1)
  #
  #[0, 1]
  #[2, 3]
  #[4, 5]
  #
  print(mat / 2)
  #
  #['1/2', '1']
  #['3/2', '2']
  #['5/2', '3']
  #
  print(mat * 2)
  #
  #[2, 4]
  #[6, 8]
  #[10, 12]
  #
  ```

##Matrix methods

  | Method | Args | What its do |
  |:-----------:|:-------:|:--------:|
  |`Matrix.transpone`| `self` | just transpone matrix |
  

  ```python
  mat.transpone()
  print(mat)
  #
  #[1,3,5]
  #[2,4,6]
  #
  ```