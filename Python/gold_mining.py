# Función que devuelve la cantidad máxima de oro que se puede obtener en una matriz
# Entrada: Matriz de posiciónes con su respectivo valor
# Salida: Diccionario con la cantidad máxima de oro que se puede obtener y la ruta que se debe seguir para obtenerlo
# Complejidad: O(n+m)
def greedy_gold_mining(C):
    path = [] # Lista de tuplas que contiene la ruta que se debe seguir para obtener la máxima cantidad de oro

    i = 0
    j = 0
    max_gold = C[i][j] # Cantidad máxima de oro que se puede obtener
    path.append((i, j))

    # Se recorre la matriz siempre y cuando no se salga de los límites de la matriz
    while i < len(C) - 1 or j < len(C[0]) - 1:
        # Se obtiene el valor de la derecha y abajo de la posición actual
        right = C[i][j + 1] if j + 1 <= len(C[0]) - 1 else 0
        bottom = C[i + 1][j] if i + 1 <= len(C) - 1 else 0
        
        # Se determina si se debe ir a la derecha o abajo en base a cual valor es mayor
        if right > bottom:
            new_max_path = (i, j + 1)
            j += 1
        elif bottom > right:
            new_max_path = (i + 1, j)
            i += 1
        else:
            if i + 1 <= len(C) - 1:
                new_max_path = (i + 1, j)
                i += 1
            else:
                new_max_path = (i, j + 1)
                j += 1
        
        # Se acumula el valor de la posición actual
        max_gold += max(right, bottom)
        # Se agrega la nueva posición a la ruta
        path.append(new_max_path)

    return { "max_gold" : max_gold, "path" : path }

def print_path(path):
    i = 0
    path_string = ""
    while i < len(path):
        if i == len(path) - 1:
            path_string += str(path[i])
        else:
            path_string += str(path[i]) + " -> "
        i += 1
    print("Path:", path_string)

def main():
    # Prueba 1
    C = [[1, 3, 3],
         [2, 1, 4],
         [0, 8, 4]]
    
    result = greedy_gold_mining(C)
    print("Cantidad máxima de oro:", result["max_gold"])
    print_path(result["path"])
    print("")

    C = [
    [0, 4, 3, 0, 2, 3, 2, 0, 0, 3],
    [1, 2, 1, 2, 0, 1, 3, 3, 3, 1],
    [3, 4, 0, 3, 3, 1, 4, 2, 1, 0],
    [1, 0, 1, 1, 2, 3, 4, 0, 3, 2],
    [4, 2, 2, 4, 1, 1, 4, 2, 1, 1],
    [2, 0, 0, 2, 4, 0, 3, 1, 1, 3],
    [2, 3, 0, 2, 0, 1, 4, 1, 3, 2],
    [3, 4, 1, 3, 0, 2, 2, 3, 3, 0],
    [1, 0, 4, 4, 0, 2, 3, 4, 1, 2],
    [2, 3, 2, 4, 2, 2, 1, 1, 1, 1]]

    result = greedy_gold_mining(C)
    print("Cantidad máxima de oro:", result["max_gold"])
    print_path(result["path"])
    print("")

    C = [
    [0, 4, 0, 1, 0, 3, 2, 4, 3, 4, 1, 0, 4, 3, 3, 4, 4, 0, 2, 1],
    [0, 1, 1, 2, 2, 0, 3, 4, 2, 0, 4, 1, 0, 1, 3, 0, 1, 1, 0, 2],
    [4, 0, 2, 2, 2, 0, 1, 4, 1, 3, 1, 4, 0, 1, 3, 0, 4, 1, 0, 3],
    [2, 0, 3, 0, 1, 1, 4, 4, 0, 4, 3, 1, 2, 2, 2, 0, 4, 3, 1, 3],
    [0, 1, 4, 1, 1, 4, 1, 3, 1, 0, 4, 3, 4, 4, 1, 1, 1, 0, 3, 0],
    [4, 1, 1, 4, 1, 2, 0, 4, 4, 3, 2, 0, 3, 2, 0, 4, 3, 2, 3, 2],
    [3, 1, 3, 3, 2, 4, 0, 3, 2, 0, 4, 4, 4, 4, 2, 1, 2, 1, 1, 1],
    [3, 0, 1, 0, 1, 0, 0, 2, 0, 4, 1, 4, 4, 3, 4, 0, 3, 4, 1, 3],
    [0, 1, 0, 3, 0, 4, 0, 1, 0, 4, 2, 1, 4, 1, 3, 4, 1, 0, 0, 1],
    [4, 3, 3, 1, 3, 4, 0, 3, 0, 0, 1, 0, 2, 1, 0, 1, 4, 4, 2, 0],
    [0, 3, 1, 3, 4, 3, 0, 2, 0, 1, 2, 2, 0, 0, 3, 0, 4, 3, 0, 2],
    [1, 1, 0, 4, 4, 4, 1, 0, 0, 0, 2, 2, 0, 0, 1, 1, 1, 0, 3, 2],
    [2, 1, 3, 1, 0, 1, 1, 1, 4, 3, 1, 2, 4, 0, 3, 1, 2, 2, 3, 3],
    [1, 2, 1, 3, 1, 1, 1, 1, 4, 2, 2, 4, 2, 2, 4, 3, 3, 1, 3, 1],
    [1, 4, 1, 2, 4, 4, 3, 1, 3, 3, 2, 3, 2, 2, 3, 2, 3, 3, 1, 3],
    [0, 1, 0, 4, 2, 4, 4, 1, 3, 0, 2, 1, 2, 2, 1, 4, 0, 3, 3, 1],
    [4, 4, 2, 0, 1, 0, 3, 0, 4, 1, 4, 3, 1, 4, 2, 2, 3, 3, 2, 4],
    [1, 0, 1, 1, 4, 1, 4, 0, 4, 3, 2, 0, 4, 4, 2, 4, 0, 1, 2, 3],
    [0, 4, 3, 4, 3, 0, 2, 0, 1, 3, 4, 2, 2, 3, 2, 3, 3, 3, 3, 2],
    [3, 1, 2, 1, 1, 1, 3, 3, 3, 4, 4, 2, 4, 3, 4, 1, 2, 0, 0, 1]]

    result = greedy_gold_mining(C)
    print("Cantidad máxima de oro:", result["max_gold"])
    print_path(result["path"])

if __name__ == '__main__':
    main()