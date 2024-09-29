import numpy as np 

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6,7, 8, 9, 10]

    arr = np.array(lista)
    print(type(arr))
    
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz2 = np.array(matriz)
    
    # print(np.array(matriz))
    
    print(arr[0])
    print(matriz2[0,2])
    print(arr[-3:])
    print(matriz2[1:,0:2])