import os
import copy
import queue

class Partial_Solution():
    def __init__(self, coins, value, upperbound):
        self.coins = coins
        self.next_unvisited = 0
        self.current_position = (0, 0)
        self.upperbound = upperbound
        self.value = value

def extend(parent_solution, C, n ,m):
    # Crear copias de la solución padre
    child1 = copy.deepcopy(parent_solution)
    child2 = copy.deepcopy(parent_solution)

    # Obtener el índice de la siguiente moneda por recolectar
    i = parent_solution.next_unvisited

    # Generar las nuevas soluciones
    row = parent_solution.current_position[0]
    col = parent_solution.current_position[1]

    # Agregar el valor de la moneda a la solución en la posición actual
    # Primero verificamos que al sumarle uno a la fila o a la columna no nos salgamos de la matriz
    # Si nos salimos de la matriz, significa que ya no hay más monedas por recolectar en esa dirección
    if row + 1 <= n:
        child1.coins[i] = (row + 1, col)
        child1.current_position = (row + 1, col)
        child1.value += C[row + 1][col]
        child1.next_unvisited = i + 1
    else:
        child1 = None

    # Usando el current_position de la solución padre, generamos la solución hija 1 y 2 para la moneda que se encuentra a la derecha y abajo
    if col + 1 <= m:
        child2.coins[i] = (row, col + 1)
        child2.current_position = (row, col + 1)
        child2.value += C[row][col + 1]
        child2.next_unvisited = i + 1
    else:
        child2 = None

    return [child1, child2]

def evaluate(child, maxMovements, C, n, m):
    # Obtener el valor de la moneda a la derecha y a la izquierda
    rightValue = C[child.current_position[0]][child.current_position[1] + 1] if child.current_position[1] + 1 <= m else 0
    leftValue = C[child.current_position[0] + 1][child.current_position[1]] if child.current_position[0] + 1 <= n else 0

    # Calcular y retornar el upperbound.
    # El upperbound es el valor de la solución actual más el valor de las monedas que faltan por recolectar multiplicado por el valor de la moneda más valiosa.
    # Esto nos permite saber que tan buena es la solución actual y si vale la pena seguir explorando esa rama
    return child.value + (maxMovements - child.next_unvisited) * max(rightValue, leftValue)

# Función que devuelve la cantidad máxima de monedas que se pueden recolectar el rebot
# Entrada: Matriz de monedas con su respectivo valor y la cantidad de filas (n) y columnas (m)
# Salida: Diccionario con la cantidad máxima de monedas recolectadas y la ruta que se debe seguir para obtenerlo
# Complejidad:
def coin_collecting(C, n, m):
    q = queue.PriorityQueue()

    # Cantidad máxima de monedas a recolectar
    M = n + m

    # Definir la solución padre
    # Calculamos el upperbound de la solución padre que es el valor de la moneda en la posición (0, 0) más el valor de las monedas que faltan por recolectar (n + m) multiplicado por el valor de la moneda más valiosa
    upperbound = C[0][0] + (n + m - 0) * max(C[0][1], C[1][0])
    root_solution = Partial_Solution([None for i in range(n + m)], C[0][0], upperbound)
    q.put((-root_solution.upperbound, 0, root_solution))

    best_so_far = copy.deepcopy(root_solution)

    counter = 0
    while not q.empty():
        # Obtener la solución padre
        parent_solution = q.get()[2]

        # Si la solución padre es mejora que la best_so_far y no se han visitado todas las monedas
        if parent_solution.upperbound > best_so_far.value and parent_solution.next_unvisited < M:
            # Obtener las nuevas soluciones, derecha y abajo
            children = extend(parent_solution, C, n, m)

            for child in children:
                # Este counter nos permite mantener el orden de las soluciones en la cola en caso de que tengan el mismo upperbound
                counter += 1

                # Si la solución hija es None, significa que no se puede seguir explorando esa rama
                if child is None:
                    continue
                
                # Calcula el upperbound de la solución hija
                child.upperbound = evaluate(child, M, C, n, m)

                # Determinar si la solucion hija es mejor que la best_so_far
                if child.value > best_so_far.value and child.next_unvisited >= M:
                    best_so_far = child

                # Si agregamos la nueva solución hija a la cola, significa que tiene mejor upperbound que la best_so_far que la best_so_far
                if child.next_unvisited < M and child.upperbound > best_so_far.value:
                    q.put((-child.upperbound, counter, child))

    return { "max_coins" : best_so_far.value, "path" : best_so_far.coins }

# Imprimir el path de la solución en base a las cordenadas de las monedas recolectadas         
def printPath(path, C):
    row = 0
    col = 0
    newPath = ""
    for i in path:
        if i[0] != row:
            row = i[0]
            newPath += "Abajo ("+str(C[row][i[1]])+")"
        else:
            col = i[1]
            newPath += "Derecha ("+str(C[i[0]][col])+")"
        
        if i != path[-1]:
            newPath += ", "

    return newPath

def main():
    coin_matrices = []
    # Toma las matrices de monedas del archivo de texto
    file_path = os.path.join(os.path.dirname(__file__), "coins-n5.txt")
    with open(file_path, "r") as file:
        matrix = []
        for line in file:
            if line == "\n":
                coin_matrices.append(matrix)
                matrix = []
                continue

            row = [int(num) for num in line.split()]
            matrix.append(row)
        coin_matrices.append(matrix)
    
    # Imprime la cantidad máxima de monedas recolectadas y la ruta que se debe seguir para obtenerlo
    for i in coin_matrices:
        print("Prueba 1:")
        result = coin_collecting(i, len(i) - 1, len(i[0]) - 1)
        print("Cantidad máxima de monedas recolectadas: " + str(result["max_coins"]))
        print("Ruta: " + printPath(result["path"], i))
        print()

if __name__ == "__main__":
    main()