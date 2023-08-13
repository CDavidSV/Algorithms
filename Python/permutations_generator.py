# Función que invierte dos elementos de una lista.
# Entrada: lista, indice i, indice j.
# Salida: lista con los elementos i y j intercambiados.
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

# Función que genera todas las permutaciones de una lista en orden lexicografico.
# Entrada: lista de elementos.
# Salida: lista de listas con todas las permutaciones de la lista de entrada.
def generate_permutations(input_list):
    if input_list == []:
        return [] # si la lista de entrada está vacía, no hay permutaciones.

    # Agregamos la lista de entrada como la primera permutación.
    permutations = []
    permutations.append(input_list)

    # Generamos las permutaciones
    while True:
        current_permutation = permutations[-1].copy()

        # Encontrar el mayor indice tal que p[i] < p[i + 1].
        current = len(current_permutation) - 1
        i = None
        # de manera decreciente buscamos el primer elemento que cumpla la condición.
        while current > 0:
            if (current_permutation[current - 1] < current_permutation[current]): # p[i] < p[i + 1].
                i = current - 1 # asignamos el indice.
                break
            current -= 1

        if i is None: # si no encontramos el indice, no hay más permutaciones.
            break
        
        # Encontrar el mayor indice j tal que p[i] < p[j].
        j = None
        right_sublist = current_permutation[i+1:]
        current = len(right_sublist) - 1
        # hacemos lo mismo que antes pero con la sublista derecha de p[i+1].
        while current >= 0:
            if (current_permutation[i] < right_sublist[current]):
                j = current + i + 1
                break
            current -= 1

        if j is None:
            break
        
        swap(current_permutation, i, j) # intercambiamos los elementos i y j.
        current_permutation = current_permutation[:i+1] + current_permutation[i+1:][::-1] # invertimos la sublista derecha de i y la concatenamos con la sublista izquierda de i.

        permutations.append(current_permutation) # agregamos la permutación a la lista de permutaciones.
    
    return permutations
    
def main():
    # Prueba 1
    input_list = [1, 2, 3, 4]
    print(generate_permutations(input_list))

    # Prueba 2
    input_list = ['a', 'b', 'c']
    print(generate_permutations(input_list))

    # Prueba 3
    input_list = [1, 1, 2]
    print(generate_permutations(input_list))

    # Prueba 4
    input_list = [5]
    print(generate_permutations(input_list))

    # Prueba 5
    input_list = []
    print(generate_permutations(input_list))

if __name__ == "__main__":
    main()