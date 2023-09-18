# Función que implementa el algoritmo de Knuth-Morris-Pratt para encontrar un patrón en un texto.
# Entrada: text y pattern, el texto y el patrón a buscar.
# Salida: Una lista de tuplas con las posiciones inicial y final de cada coincidencia.
# Complejidad: O(n + m), donde n es la longitud del texto y m la longitud del patrón.
def KMP(text, pattern):

    # Calcula la lista LPS (Longest Prefix Suffix) para el patron dado.
    # Entrada: pattern, el patrón a buscar.
    # Salida: Una lista con los valores de LPS.
    # Complejidad: O(m)
    def calculateLPS(pattern):
        # Inicializar la lista LPS con ceros.
        LPS = [0 for i in range(len(pattern))]
            
        # Recorremos el patron desde el segundo elemento.
        j = 0
        counter = 1
        for i in range(1, len(pattern) - 1):
            # Si el elemento actual es igual al elemento en la posición j, entonces
            # el elemento en la posición i de la lista LPS es igual a counter.
            if pattern[i] == pattern[j]:
                LPS[i] = counter
                counter += 1
                j += 1
            else: # Si no son iguales, entonces reiniciamos el contador.
                counter = 1
        
        return LPS

    # Obtener la longitu d del patron y el texto.
    textLength = len(text)
    patternLength = len(pattern) 
    
    # Calcular la lista LPS.
    LPS = calculateLPS(pattern)

    matches = []

    i = 0
    j = 0
    # Recorremos el texto mientras no se haya llegado al final.
    while i < textLength:
        # Si son iguales, avanzamos en ambos.
        if text[i] == pattern[j]:
            i += 1
            j += 1
        elif j > 0: # Si no son iguales y j > 0, retrocedemos j dependiendo de la posición en el arreglo LPS.
            j = LPS[j - 1]
        else:
            i += 1

        # Cuando se consigue una coincidencia
        if j == patternLength:
            # Guardamos la posición de la coincidencia y retrocedemos j.
            matches.append((i - patternLength, i - 1))
            j = LPS[j - 1]

    return matches

def main():
    # Prueba 1
    text = "paypaypal"
    pattern = "paypal"

    print("Patrones (comienzo, fin):", KMP(text, pattern))

if __name__ == '__main__':
    main()