
# Algoritmo de coloreo de grafos usando greedy.
# Entrada: Grafo en lista de adyacencia
# Salida: Numero de colores usados y lista de colores de cada nodo
# Complejidad: O(n^2)
def greedy_graph_coloring(graph):
    node_colors = []
    used_colors = []
    k = 0

    # Inicializar listas de colores, que colores le corresponden a cada nodo y si un color ya fue usado
    for i in range(len(graph)):
        node_colors.append(None)
        used_colors.append(False)

    for index, node in enumerate(graph):
        # Buscamos el color que no se haya usado en los vecinos
        color = 0
        for neighbor in node:
            if node_colors[neighbor] is None or node_colors[neighbor] != color:
                node_colors[index] = color

                # Si es la primera vez que se usa el color, se marca como usado
                if not used_colors[color]:
                    used_colors[color] = True
                    k += 1 # Incrementamos el numero de colores usados
                break
            else:
                color += 1
    
    return k, node_colors

# Algoritmo de coloreo de grafos usando Welsh-Powell.
# Entrada: Grafo en lista de adyacencia
# Salida: Numero de colores usados y lista de colores de cada nodo
# Complejidad: O(n^2)
def welsh_powell(graph):
    # Ordenar el grafo en orden no creciente de grado
    graph.sort(key=lambda x: len(x))

    processed = []
    node_colors = []
    # Inicializar listas de colores, que colores le corresponden a cada nodo y si un color ya fue usado
    for i in range(len(graph)):
        processed.append(False)
        node_colors.append(None)

    color = 0
    for index, neighbors in enumerate(graph):
        if not processed[index]:
            processed[index] = True
            node_colors[index] = color
        
            for j in range(len(graph)):
                if j not in neighbors and not processed[j]:
                    processed[j] = True
                    node_colors[j] = color
            color += 1
    
    return color, node_colors

def main():
    graph_1 = [
        [1, 3, 2],
        [0, 2, 4],
        [0, 1, 3, 4],
        [0, 2, 4],
        [1, 2, 3]
    ]
    
    k = greedy_graph_coloring(graph_1)
    print(k)

    k = welsh_powell(graph_1)
    print(k)

if __name__ == '__main__':
    main()