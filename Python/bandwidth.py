import os
import random

# Preguntas:
# ¿Cómo se podría mejorar este algoritmo para producir mejores soluciones con las mismas iteraciones?
# R = Se podria interntar buscar otra forma de obtener nuevos ordenes en los vertices en vez de desordenarlos. 
# Se poodria hacer swaps aleatorios entre los vertices o partir la lista de vertices en dos y mezclarlas.

# ¿Cuántas soluciones posibles hay para este problema (en función de n)?
# R = Serian n! soluciones posibles, ya que cada vertice puede estar en n posiciones diferentes.

# ¿Cuál es la dificultad del problema? (no de tu algoritmo)
# R = Este problema es NP-Complete, por lo que no se conoce un algoritmo que lo resuelva en tiempo polinomial.

def parse_graph_file(file_path):
    # Abrimos el archivo
    absolute_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(absolute_path, 'r') as f:
        lines = f.read().splitlines()

    # Creamos el grafo como una lista de adyacencia
    num_vertices = int(lines[0].split(' ')[0])
    graph = [[] for _ in range(num_vertices)]
    vertices = list(range(num_vertices))

    # Agregamos los vertices al grafo y las aristas
    for line in lines[1:]:
        edge = line.split(' ')
        vertex1, vertex2 = int(edge[0]), int(edge[1])

        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)

    return graph, vertices

# Calcula el ancho de banda maximo
def calculate_max_bandwidth(graph, vertices):
    max_distance = 0

    # Creamos un diccionario para obtener el indice de un vertice
    vertex_indices = {vertex: index for index, vertex in enumerate(vertices)}

    # Recorremos el grafo y calculamos la distancia entre los vertices adyacentes
    for i in range(len(vertices)):

        # Obtenemos los vecinos del vertice
        neighbors = graph[vertices[i]]

        # Recorremos los vecinos y calculamos la distancia
        for j in range(len(neighbors)):
            distance = abs(i - vertex_indices[neighbors[j]])
            # Si la distancia es mayor al maximo, lo reemplazamos
            max_distance = max(max_distance, distance)
    
    return max_distance

def main():
    graph, vertices = parse_graph_file("grafo-pres-24.txt")
    steps = 100
    
    # Calculamos el ancho de banda maximo y minimo con el orden inicial
    min_bandwidth = calculate_max_bandwidth(graph, vertices)
    max_bandwidth = min_bandwidth

    # Iteramos la cantidad de pasos especificada
    for _ in range(steps):
        # Desordenamos los vertices
        random.shuffle(vertices)
        
        # Calculamos el ancho de banda maximo y minimo
        curr_bandwidth = calculate_max_bandwidth(graph, vertices)

        # Si el ancho de banda actual es menor al minimo, lo reemplazamos
        if curr_bandwidth < min_bandwidth:
            min_bandwidth = curr_bandwidth

        # Si el ancho de banda actual es mayor al maximo, lo reemplazamos
        if curr_bandwidth > max_bandwidth:
            max_bandwidth = curr_bandwidth
    
    print("Min bandwidth:", min_bandwidth)
    print("Max bandwidth:", max_bandwidth)

if __name__ == "__main__":
    main()