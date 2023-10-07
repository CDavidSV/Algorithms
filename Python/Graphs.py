import os

# Funcion para leer el archivo de texto con la matriz de adyacencia
# Entrada: La ruta del archivo de texto
# Salida: Retorna la matriz de adyacencia, la lista de adyacencia y los nombres de los nodos
def read_graph_from_file(file_path):
    file_path = os.path.dirname(__file__) + '/' + file_path

    # Una cadena con los nombres de los nodos alfabético
    node_names = 'abcdefghijklmnopqrstuvwxyz'

    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Generar el adjacency matrix
    adjacency_matrix = []
    for line in lines:
        adjacency_matrix.append([int(x) for x in line.split()])
    
    # Generar el adjacency list
    adjacency_list = []
    for line in lines:
        node_list = []
        for i, node in enumerate(line.split()):
            if int(node) > 0:
                node_list.append((i, int(node)))
        adjacency_list.append(node_list)

    return adjacency_matrix, adjacency_list, node_names[0:len(adjacency_matrix)]

# Funcion para imprimir el camino mas corto desde un nodo inicial hasta un nodo final
# Entrada: El arreglo de distancias, el arreglo de desde donde se llega a cada nodo, el arreglo de nombres de nodos y el nodo final
# Salida: Imprime el camino mas corto desde el nodo inicial hasta el nodo final
def print_path(distances, fromNode, node_names, end):
    curr_node = end
    total_distance = 0
    path = []

    # Recorrer el arreglo de nodos desde donde se llega a cada nodo hasta llegar al nodo inicial
    while curr_node is not None:
        total_distance += distances[curr_node] # Incrementar la distancia total
        path.append((curr_node, distances[curr_node]))
        curr_node = fromNode[curr_node]

    path.reverse()

    # Generamos la cadena de texto con el camino de manera mas legible
    path_string = ''
    for i in path:
        path_string += f'{node_names[i[0]]}({i[1]})'

        if i[0] == end:
            path_string += f': {total_distance}'
        else:
            path_string += ', '

    print(path_string)

# Funcion para encontrar el nodo con menor distancia que no haya sido procesado
def find_min_processed_node(distances, processed):
    min = float('inf')
    min_index = None
    # Encontrar el indice del nodo con menor distancia pero que no haya sido procesado
    for i, v in enumerate(distances):
        if v < min and not processed[i]:
            min = v
            min_index = i

    return min_index

# Implementacion del algoritmo de Dijkstra
# Entrada: La lista de adyacencia, el nodo inicial y el nodo final
# Salida: Retorna las distancias desde el nodo inicial hasta cada nodo y el arreglo de desde donde se llega a cada nodo
# Complejidad: O(V^2)
def dijkstra(adjacency_list, start, end):
    # Arreglo de distancias desde un nodo al otro
    distances = [float('inf') for i in range(len(adjacency_list))]
    distances[start] = 0

    # Arreglos de nodos procesados y desde donde se llega a cada nodo
    visited = [False for i in range(len(adjacency_list))]
    fromSource = [None for i in range(len(adjacency_list))]
    
    for _ in range(len(adjacency_list)):
        # Obtenemos un nodo no procesado con la menor distancia
        u = find_min_processed_node(distances, visited)
        visited[u] = True

        # Recorrer cada vecino de el nodo u
        for neighbor, weight in adjacency_list[u]:
            new_distance = distances[u] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                fromSource[neighbor] = u
    
    # Retornar las distancias y el arreglo desde donde se llega a cada nodo
    return distances, fromSource

# Implementacion del algoritmo de Prim
# Entrada: La lista de adyacencia
# Salida: Retorna las distancias desde el nodo inicial hasta cada nodo y el arreglo de desde donde se llega a cada nodo para el arbol
# Complejidad: O(V^2)
def prim(adjacency_list):
    distances = [float('inf') for i in range(len(adjacency_list))]
    distances[0] = 0

    visited = [False for i in range(len(adjacency_list))]
    fromSource = [None for i in range(len(adjacency_list))]

    # Aqui en vez de recorrer todos los nodos, recorremos todos los nodos que no han sido procesados
    while False in visited:
        # Aqui de igual manera obtenemos el nodo con la menor distancia
        u = find_min_processed_node(distances, visited)
        visited[u] = True

        for neighbor, weight in adjacency_list[u]:
            if not visited[neighbor] and weight < distances[neighbor]:
                distances[neighbor] = weight
                fromSource[neighbor] = u
    
    return distances, fromSource

# Implementacion del algoritmo de Warshall
# Entrada: La matriz de adyacencia
# Salida: Retorna la matriz de adyacencia con los caminos entre cada nodo
# Complejidad: O(V^3)
def warshall(adjacency_matrix):
    for k in range(len(adjacency_matrix)):
        for i in range(len(adjacency_matrix)):
            for j in range(len(adjacency_matrix)):
                adjacency_matrix[i][j] = adjacency_matrix[i][j] or (adjacency_matrix[i][k] and adjacency_matrix[k][j])

    return adjacency_matrix

# Implementacion del algoritmo de Floyd
# Entrada: La matriz de adyacencia
# Salida: Retorna la matriz de adyacencia con los caminos entre cada nodo
# Complejidad: O(V^3)
def floyd(adjacency_matrix):
    # Inicializar la diagonal de la matriz de adyacencia en 0 y los 0 en infinito
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            # Si no hay conexion entre los nodos, se pone infinito siempre y cuando no sea en la diagonal
            if adjacency_matrix[i][j] == 0 and i != j:
                adjacency_matrix[i][j] = float('inf')
            elif i == j:
                adjacency_matrix[i][j] = 0 # Poner la diagonal en 0
    
    for k in range(len(adjacency_matrix)):
        for i in range(len(adjacency_matrix)):
            for j in range(len(adjacency_matrix)):
                adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])
    
    return adjacency_matrix

def main():
    _, adjacency_list, node_names = read_graph_from_file('graph1.txt')

    print('--------------- Prueba de Prim ---------------')
    distances, fromSource = prim(adjacency_list)
    print("Costo total del arbol:", sum(distances))
    for i in range(1, len(fromSource)):
        if fromSource[i] is not None:
            print(f"{node_names[fromSource[i]]} -> {node_names[i]}: {distances[i]}")

    _, adjacency_list, node_names = read_graph_from_file('graph2.txt')
    print('\n------------- Prueba de Dijkstra -------------')
    
    for i in range(1, len(adjacency_list)):
        distances, fromSource = dijkstra(adjacency_list, 0, i)
        print('Camino mas corto desde', node_names[0], 'hasta', node_names[i], end=': ')
        print_path(distances, fromSource, node_names, i)

    adjancency_matrix, _, node_names = read_graph_from_file('graph3.txt')
    print('\n------------- Prueba de Warshall -------------')
    adjacency_matrix = warshall(adjancency_matrix)
    for i in range(len(adjacency_matrix)):
        string = f"{node_names[i]} tiene un camino hacia: "
        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[i][j] >= 1:
                string += f"{node_names[j]}"
                if j != len(adjacency_matrix) - 1:
                    string += ', '
        print(string)
    
    adjancency_matrix, _, node_names = read_graph_from_file('graph4.txt')
    print('\n-------------- Prueba de Floyd ---------------')
    adjacency_matrix = floyd(adjancency_matrix)
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if i != j:
                if adjacency_matrix[i][j] == float('inf'):
                    print(f"No hay camino de {node_names[i]} hacia {node_names[j]}")
                else:
                    print(f"Desde '{node_names[i]}' hacia '{node_names[j]}' el costo es de {adjacency_matrix[i][j]}")
    
    # ¿Cómo harías para reconstruir el camino? 
    # Para poder reconstruir el camino, se puede hacer otra matriz que guarde el nodo anterior a cada nodo, de esta manera se puede reconstruir el camino
    # de manera similar a como se hace en Dijkstra para cada nodo. Simplemente habria que guardar el nodo anterior a cada nodo en la matriz y luego recorrer
    # la matriz para reconstruir el camino segun el nodo incial y el nodo final elegidos.

if __name__ == "__main__":
    main()