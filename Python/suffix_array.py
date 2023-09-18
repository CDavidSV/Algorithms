# Función que calcula el suffix array de una cadena.
# Entrada: Una cadena de caracteres.
# Salida: Una lista de enteros que representan los indices de los sufijos ordenados de la cadena de entrada.
# Complejidad: O(n*k*log(n)) donde n*log(n) es la complejidad del algoritmo para ordenar y k el la longitud máxima de una cadena dentro del arreglo
def suffix_array(inputString):
    # Primero generar la lista de sufijos de la cadena de entrada
    suffixes = [inputString[i:] for i in range(len(inputString))]
    
    # Ordenar la lista de sufijos
    sortedSuffixes = sorted(suffixes)

    # Retornar la lista de indices de los sufijos ordenados
    return [suffixes.index(i) for i in sortedSuffixes]

def main():
    inputString = "anabanana"
    print(suffix_array(inputString))

if __name__ == '__main__':
    main()