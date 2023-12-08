import os
import random


def parse_graph_file(file_path):
  # Abrimos el archivo
  absolute_path = os.path.join(os.path.dirname(__file__), file_path)
  with open(absolute_path, 'r') as f:
    lines = f.read().splitlines()

  # Creamos el grafo como una lista de adyacencia
  num_vertices = int(lines[0].split(' ')[0])
  vertices = list(range(num_vertices))
  edges = [(int(edge.split(' ')[0]) - 1, int(edge.split(' ')[1]) - 1)
           for edge in lines[1:]]

  return vertices, edges


# Calcula el ancho de banda maximo
def calculate_min_bandwidth(edges, vertices):
  min_distance = float('inf')
  distances = {}
  vertex_indexes = {vertex: index for index, vertex in enumerate(vertices)}

  # Recorremos todas las aristas
  for edge in edges:
    distance = abs(vertex_indexes[edge[0]] - vertex_indexes[edge[1]])
    distances[edge] = distance
    min_distance = min(min_distance, distance)

  return min_distance, distances


def recalculate_min_distance(edges, vertices, distances, i, j):
  # Encontrar las aristas que cambia despues de intercambiar los vertices i y j
  connected_edges = [edge for edge in edges if i in edge or j in edge]
  vertex_indexes = {vertex: index for index, vertex in enumerate(vertices)}

  # Recalcular las distancias de las aristas que cambiaron
  for edge in connected_edges:
    new_distance = abs(vertex_indexes[edge[0]] - vertex_indexes[edge[1]])
    distances[edge] = new_distance

  # Volver a encontrar el minimo
  min_distance = min(distances.values())

  return min_distance, distances


# Incrementa la solución actual intercambiando dos vertices de manera aleatoria
def rand_vertex_swap(edges, vertices, distances):
  # Seleccionar dos vertices al azar
  i, j = random.sample(range(len(vertices)), 2)

  # Intercambiarlos
  temp = vertices[i]
  vertices[i] = vertices[j]
  vertices[j] = temp

  # Aqui se recalcula la distancia minima en unicamente los nodos intercambiados
  min_distance, distances = recalculate_min_distance(edges, vertices,
                                                     distances, vertices[i],
                                                     vertices[j])
  return vertices, min_distance, distances


def save_results(solutions, fileName):
  file_path = f"resultados/{fileName}_resultados.txt"
  absolute_path = os.path.join(os.path.dirname(__file__), file_path)
  with open(absolute_path, 'w') as f:
    f.write(f"Soluciones Anti-Bandwidth para {fileName}.txt:\n")
    for index, solution in enumerate(solutions):
      f.write(f"Solucion {index + 1}:\nAncho de Banda: {solution}\n")


def main(fileName):
  fileName = "ibm32"  # Cambiar este al nombre correspondiente del archivo a probar sin el sufijo
  vertices, edges = parse_graph_file(fileName + ".txt")

  steps = 100_000  # Cantidad de pasos
  solutions = 50  # Cantidad de soluciones
  solutions_list = []

  for _ in range(solutions):
    # Calculamos el ancho de banda maximo y minimo con el orden inicial
    random.shuffle(vertices)
    max_bandwidth, distances = calculate_min_bandwidth(edges, vertices)
    curr_bandwidth = max_bandwidth

    # Iteramos la cantidad de pasos especificada
    for _ in range(steps):
      # Desordenamos los vertices
      vertices, curr_bandwidth, distances = rand_vertex_swap(
          edges, vertices, distances)

      # Si el ancho de banda actual es mayor al maximo, lo reemplazamos
      if curr_bandwidth > max_bandwidth:
        max_bandwidth = curr_bandwidth
    solutions_list.append(max_bandwidth)

  # Imprimimos la solucion mas optima de las 50
  best = max(solutions_list)
  print(f"Mejor solución encontrada para {fileName}.txt")
  print(f"Solución {solutions_list.index(best) + 1}:")
  print("Ancho de banda:", best)

  # Guardar los resultados en un archivo
  save_results(solutions_list, fileName)


if __name__ == "__main__":
  main()