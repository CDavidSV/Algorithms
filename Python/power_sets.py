# Función que recursivamente genera el conjunto potencia de n elementos.
# Entrada: n, entero positivo.
# Salida: lista de listas con el conjunto potencia de n elementos.
# Complejidad: O(2^n)
def power_set_bin(n):
    # Caso base
    if n == 1:
        return [[0], [1]] # el conjunto potencia de 1 elemento es {0, 1}.
    else:
        l1 = power_set_bin(n - 1) # Recursivamente generamos el conjunto potencia de n - 1 elementos.
        l2 = [list(inner) for inner in l1]
        l2.reverse() # Copia de la lista l1 invertida.

        for i in range(len(l1)): # Agregamos 0 al inicio de cada lista de l1 y 1 al inicio de cada lista de l2. 
            l1[i].insert(0, 0)
            l2[i].insert(0, 1)

        return l1 + l2 # Concatenamos las listas l1 y l2.

def main():
    # Pruebas
    print(power_set_bin(1))
    print(power_set_bin(2))
    print(power_set_bin(3))
    print(power_set_bin(4))

if __name__ == '__main__':
    main()