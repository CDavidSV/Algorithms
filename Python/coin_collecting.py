# Función que devuelve la cantidad máxima de monedas que se pueden recolectar el rebot
# Entrada: Matriz de 0 y 1, donde 1 representa una moneda
# Salida: Cantidad máxima de monedas recolectadas
# Complejidad: O(n*m)
def coin_collecting_tabu(C):
    T = [[0 for i in range(len(C[0]) + 1)] for i in range(len(C) + 1)]

    for i in range(1, len(T)):
        for j in range(1, len(T[0])):
            T[i][j] = max(T[i - 1][j], T[i][j - 1]) + C[i - 1][j - 1]
    
    return T[i][j]

def main():
    C = [[0, 0, 0, 0, 1],
         [0, 1, 0, 1, 0],
         [0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0],
         [1, 0, 0, 0, 1]]
    
    print("Cantidad máxima de monedas recolectadas:", coin_collecting_tabu(C))

if __name__ == '__main__':
    main()