# Función helper para el algoritmo de ordenamiento merge sort.
# Entrada: Lista, índice de inicio, índice de la mitad y índice final.
# Salida: Lista ordenada.
def merge(list, L, M):
    # Inicializar los índices de las dos mitades de la lista, incluyendo el índice de la lista original
    i, j, k = 0, 0, 0

    # Determinar el menor elemento de las dos mitades de la lista y agregarlo a la lista original
    while i < len(L) and j < len(M):
        if L[i] <= M[j]: # El elemento de la primera mitad es menor o igual al elemento de la segunda mitad
            list[k] = L[i]
            i += 1
        else: # El elemento de la segunda mitad es menor al elemento de la primera mitad
            list[k] = M[j]
            j += 1
        k += 1

    # Agregar los elementos restantes.
    while i < len(L):
        list[k] = L[i]
        i += 1
        k += 1

    while j < len(M):
        list[k] = M[j]
        j += 1
        k += 1
    
    return list

# Algoritmo de ordenamiento merge sort.
# Entrada: Lista de elementos desordenados.
# Salida: Lista de elementos ordenados.
# Complejidad: O(n*log(n))
def mergeSort(list):
    if len(list) > 1: # Determinar si la lista tiene más de un elemento
        half = len(list) // 2

        # Hacer copias de las dos mitades de la lista
        L = list[0:half]
        M = list[half:]

        L = mergeSort(L)
        M = mergeSort(M)
        list = merge(list, L, M) # Unir las dos mitades de la lista
    
    return list


def main():
    # Prueba 1
    testList = [5, 4, 3, 2, 1]
    print(mergeSort(testList))

    # Prueba 2
    testList = [4, 3, 5, 6, 2, 3, 4]
    print(mergeSort(testList))

    # Prueba 3
    testList = [6,5,2,7,4,8,9,10,11,22,3,5]
    print(mergeSort(testList))

    # Prueba 4
    testList = [0, -2]
    print(mergeSort(testList))

if __name__ == "__main__":
    main()