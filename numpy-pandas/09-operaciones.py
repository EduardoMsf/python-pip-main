import numpy as np 

# Example 1: Multiplying a list by a scalar
lista = [1,2]
print(lista*2)  # Output: [1, 2, 1, 2]

# Example 2: Performing element-wise multiplication and addition on a NumPy array
arr = np.arange(0,10)
arr2 = arr.copy()
print(arr2*2)  # Output: [0 2 4 6 8 10 12 14 16 18]
print(arr2+2)  # Output: [2 3 4 5 6 7 8 9 10 11]

# Example 3: Performing matrix multiplication using NumPy
matriz = arr.reshape(2,5)
matriz2 = matriz.copy()
print(np.matmul(matriz,matriz2.T))  # Output: [[30 80] [80 255]]
print(matriz @ matriz2.T)  # Output: [[30 80] [80 255]]
