import random

def ordenamiento_por_insercion(lista):
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

if __name__ == '__main__':
    tamano_lista = int(input('¿De qué tamaño sera la lista? '))
    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)
    ordenamiento_por_insercion(lista)
    print(lista)