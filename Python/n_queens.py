import queue
import copy

class Partial_Solution:
    def __init__(self, queens):
        self.queens = queens
        self.next_unvisited = 0

# Función que genera las nuevas soluciones a partir de una solución padre.
# Entrada: solucion padre, fila en la que se colocará la reina, tamaño del tablero
# Salida: lista de soluciones
def extend(parent_solution, row, n):
    new_solutions = []

    # Genera una nueva solución por cada columna posible.
    for i in range(n):
        # Copia la solución padre y agrega la nueva reina.
        new_solution = copy.deepcopy(parent_solution)
        
        # Agrega la nueva reina a la solución.
        new_solution.queens[parent_solution.next_unvisited] = (row, i)
        new_solution.next_unvisited = parent_solution.next_unvisited + 1
        new_solutions.append(new_solution)
    
    return new_solutions

# Función que genera una solucion al problema de las n reinas
# Entrada: n, el tamaño del tablero
# Salida: un objeto de tipo Queen_Board con la solución
# Complejidad: O(n!)
def n_queens(n):
    # Función que genera un string con el tablero de ajedrez
    def generate_board(queens, n):
        board_string = ""

        for i in range(n):
            for j in range(n):
                if queens[i][1] == j:
                    board_string += "♕ "
                else:
                    board_string += "▢ "
            board_string += "\n"
        return board_string

    # Función que verifica si una reina se puede colocar en una posición
    def is_placeable(queens, row, col):
        for queen in queens:

            # Verifica si la reina está en la misma columna o en diagonal con otra reina.
            if queen is not None and (abs(queen[0] - row) == abs(queen[1] - col) or abs(queen[1] - col) == 0):
                return False
        return True

    # Genera la solución inicial
    root_solution = Partial_Solution([None for i in range(n)])
    
    q = queue.Queue()
    q.put(root_solution)

    # El algoritmo termina cuando ya no hay soluciones por visitar.
    while not q.empty():
        solution = q.get()
        queens = solution.queens
        unvisited = solution.next_unvisited

        # Si ya se visitaron todas las reinas, se genera el tablero.
        if unvisited < n:
            # Genera las nuevas soluciones.
            children = extend(solution, unvisited, n)
            
            # Para cada nueva solución, verifica si se puede colocar la reina en la posición y lo agrega a la fila.
            for child in children:
                if is_placeable(queens, child.queens[unvisited][0], child.queens[unvisited][1]):
                    q.put(child)

    return generate_board(queens, n)

def main():
    # Prueba 1
    board = n_queens(4)
    print(board)

    # Prueba 2
    board = n_queens(6)
    print(board)

    # Prueba 3
    board = n_queens(8)
    print(board)

if __name__ == "__main__":
    main()