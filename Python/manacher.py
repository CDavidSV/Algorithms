def longestPalindrome(inputString):
    # Declarar el centro y el liminte inicial
    center = limit = 0
    
    # Generar la cadena modificada y el arreglo p
    p_string = '@$' + '$'.join(inputString) + '$#'
    p = [0 for i in range(len(p_string))]

    print(p_string)

    # Recorrer la cadena modificada
    for i in range(1, len(p) - 1):
        # Cuando i esta dentro del limite, se copia el valor segun la simetria
        if i < limit:
            p[i] = min(limit - i, p[2 * center - i])

        # Se siguen buscando palindromos apartir de i
        gap = p[i] + 1
        while p_string[i - gap] == p_string[i + gap]:
            p[i] += 1
            gap += 1

        # Si el limite se excede, se actualiza el centro y el limite
        if i + p[i] > limit:
            center = i
            limit = i + p[i]
    
    largest_palindrome = max(p)
    index_largest_palindrome = p.index(largest_palindrome)

    startingIndex = (index_largest_palindrome - p[index_largest_palindrome]) // 2


    return { 'largest_palindrome': largest_palindrome, 'starting_index': startingIndex, 'ending_index': startingIndex + largest_palindrome - 1}

def main():
    inputString = "aaaa"
    print(longestPalindrome(inputString))

if __name__ == '__main__':
    main()