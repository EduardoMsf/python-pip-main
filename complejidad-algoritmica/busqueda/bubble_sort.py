import random
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == '__main__':
    tamano_lista = int(input('¿De qué tamaño sera la lista? '))
    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)
    print(bubble_sort(lista))