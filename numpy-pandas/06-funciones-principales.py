import numpy as np

# Genera un array de 10 números enteros aleatorios entre 1 y 19
arr = np.random.randint(1, 20, 10)

# Reorganiza el array en una matriz de 2 filas y 5 columnas
matriz = arr.reshape(2, 5)

# Imprime la matriz
print(matriz)

# Imprime el valor máximo del array
print(arr.max())

# Imprime el valor máximo de cada fila de la matriz
print(matriz.max(1))

# Imprime el valor máximo de cada columna de la matriz
print(matriz.max(0))

# Imprime el índice del valor máximo de cada columna de la matriz
print(matriz.argmax(0))

# Imprime el índice del valor máximo de cada fila de la matriz
print(matriz.argmax(1))

# Imprime el índice del valor máximo del array
print(arr.argmax())

# Imprime el valor mínimo del array
print(arr.min())

# Imprime el valor mínimo de cada fila de la matriz
print(matriz.min(1))

# Imprime el valor mínimo de cada columna de la matriz
print(matriz.min(0))

# Imprime el índice del valor mínimo de cada columna de la matriz
print(matriz.argmin(0))

# Imprime el índice del valor mínimo de cada fila de la matriz
print(matriz.argmin(1))

# Imprime el índice del valor mínimo del array
print(arr.argmin())

# Imprime el rango (peak-to-peak) del array
print(arr.ptp())

# Imprime el rango (peak-to-peak) de cada columna de la matriz
print(matriz.ptp(0))

# Imprime el percentil 50 (mediana) del array
print(np.percentile(arr, 50))

# Ordena el array en su lugar
arr.sort()

# Imprime el array ordenado
print(arr)

# Imprime la mediana del array
print(np.median(arr))

# Imprime la mediana de cada columna de la matriz
print(np.median(matriz, 0))

# Imprime la mediana de cada fila de la matriz
print(np.median(matriz, 1))

# Imprime la desviación estándar del array
print(arr.std())

# Imprime la varianza del array (desviación estándar al cuadrado)
print(arr.std()**2)

# Imprime la varianza del array
print(arr.var())

# Imprime la media del array
print(np.mean(arr))

# Crea un array 2x2
a = np.array([[1, 2], [3, 4]])

# Crea un array de 1x2
b = np.array([5, 6])

# Imprime las dimensiones de los arrays a y b
print(a.ndim, b.ndim)

# Expande las dimensiones de b para que sea 2D (1x2)
b = np.expand_dims(b, axis=0)

# Concatena a y b a lo largo de las filas (axis=0)
print(np.concatenate((a, b), axis=0))

# Concatena a y la transpuesta de b a lo largo de las columnas (axis=1)
print(np.concatenate((a, b.T), axis=1))