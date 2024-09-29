import numpy as np


list(range(0, 10))

# Crea un array de números del 0 al 8 con un paso de 2
print(np.arange(0, 10, 2))

# Crea una matriz de 10x10 llena de ceros
print(np.zeros((10, 10)))

# Crea una matriz de 10x10 llena de unos
print(np.ones((10, 10)))

# Crea un array de 10 números equidistantes entre 0 y 10
print(np.linspace(0, 10, 10))

# Crea una matriz identidad de 4x4
print(np.eye(4))

# Crea una matriz de 4x4 con números aleatorios entre 0 y 1
print(np.random.rand(4, 4))

# Crea una matriz de 10x10 con números enteros aleatorios entre 1 y 99
print(np.random.randint(1, 100, (10, 10)))