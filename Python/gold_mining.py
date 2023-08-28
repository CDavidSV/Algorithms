# Función que devuelve la cantidad máxima de oro que se puede obtener en una matriz
# Entrada: Matriz de posiciónes con su respectivo valor
# Salida: Cantidad máxima de oro que se puede obtener
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
            new_max_path = (i + 1, j)
            i += 1
        
        # Se acumula el valor de la posición actual
        max_gold += max(right, bottom)
        # Se agrega la nueva posición a la ruta
        path.append(new_max_path)

    return { "max_gold" : max_gold, "path" : path }

def main():
    # Prueba 1
    C = [[1, 3, 3],
         [2, 1, 4],
         [0, 8, 4]]
    
    greedy_gold_mining(C)

if __name__ == '__main__':
    main()