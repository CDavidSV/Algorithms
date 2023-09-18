# Función que implementa el algoritmo de Z para encontrar un patrón en un texto.
# Entrada: text y pattern, el texto y el patrón a buscar.
# Salida: Una lista de tuplas con las posiciones inicial y final de cada coincidencia.
# Complejidad: O(n + m)
def Z_Algorith(text, pattern):

    # Función que calcula el Z array para un texto dado.
    # Entrada: text, el texto a analizar y el patron
    # Salida: Z Array
    def calculate_Z_Array(pattern, text):
        X = len(pattern) + len(text) + 1
        Z = [0 for i in range(X)]
        C = pattern + "$" + text

        L = 0
        R = 0
        for i in range(1, X):
            # Si el valor de i es menor que R (limite del Z-Box)
            if i <= R:
                k = i - L
                if Z[k] < R - i + 1:
                    Z[i] = Z[k]
                else:
                    while R < X and C[R - L] == C[R]:
                        R += 1
                    Z[i] = R - L
                    R -= 1
            else:
                # Cuando i sea mayor que R
                L = R = i
                # Comapramos los caracteres hasta que no coincidan
                while R < X and C[R - L] == C[R]:
                    R += 1

                # Almacenamoz en Z[i] el valor de R - L que es la cantidad de caracteres coincidentes
                Z[i] = R - L
                R -= 1
        
        return Z
    
    # Se calcula el z array
    Z = calculate_Z_Array(pattern, text)
    matches = []

    # Recorremos el Z array y buscamos los valores que sean iguales al largo del patron
    for i in range(len(Z)):
        if Z[i] == len(pattern):
            matches.append((i - len(pattern) - 1, i - len(pattern) -1 + len(pattern) - 1))
    
    return matches

def main():
    # Prueba 1
    text = "abaxabab"
    pattern = "ab"

    print(Z_Algorith(text, pattern))

if __name__ == '__main__':
    main()