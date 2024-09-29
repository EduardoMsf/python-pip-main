import numpy as np

if __name__ == "__main__":
    scalar = np.array(42)
    print(scalar)
    print(scalar.ndim)
    
    vector = np.array([1, 2, 3, 4, 5])
    print(vector)
    print(vector.ndim)
    
    matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matriz)
    print(matriz.ndim)
    
    tensor = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
    print(tensor)
    print(tensor.ndim)
    
    """Agregar dimensiones"""
    vector = np.array([1, 2, 3, 4, 5], ndmin=10)
    print(vector)
    print(vector.ndim)
    
    expand = np.expand_dims(vector, axis=0)
    print(expand)
    print(expand.ndim)
    
    print(vector, vector.ndim)
    vector_2 = np.squeeze(vector)
    print(vector_2, vector_2.ndim)