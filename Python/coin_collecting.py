# Función que devuelve la cantidad máxima de monedas que se pueden recolectar el rebot
# Entrada: Matriz de 0 y 1, donde 1 representa una moneda
# Salida: Cantidad máxima de monedas recolectadas
# Complejidad: O(min(m,n)^2)
def coin_collecting_tabu(C):
    # Genera una matriz de tamaño n+1 y m+1, donde n y m son las dimensiones de la matriz que contiene las monedas.
    # En esta matriz se almacena la cantidad máxima de monedas que se pueden recolectar hasta esa posición.
    T = [[0 for i in range(len(C[0]) + 1)] for i in range(len(C) + 1)]

    # Calcula la cantidad máxima de monedas que se pueden recolectar en cada posición de la matriz T.
    for i in range(1, len(T)):
        for j in range(1, len(T[0])):
            T[i][j] = max(T[i - 1][j], T[i][j - 1]) + C[i - 1][j - 1] # Relación de recurrencia
    
    return T[i][j]

def main():
    C = [[0, 0, 0, 0, 1],
         [0, 1, 0, 1, 0],
         [0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0],
         [1, 0, 0, 0, 1]]
    
    print(C)
    print("Cantidad máxima de monedas recolectadas:", coin_collecting_tabu(C))

    C = [[0, 0, 0, 0, 1],
         [0, 1, 0, 1, 0],
         [0, 0, 0, 1, 0],
         [0, 0, 1, 0, 1],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 0, 1]]
    
    print(C)
    print("Cantidad máxima de monedas recolectadas:", coin_collecting_tabu(C))

if __name__ == '__main__':
    main()