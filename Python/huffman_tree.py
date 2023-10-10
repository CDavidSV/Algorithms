import os

class Node:
    def __init__(self, char, prob) -> None:
        self.char = char
        self.prob = prob

        self.left = None
        self.right = None

class Tree:
    def __init__(self, root) -> None:
        self.root = root
    
    # Usamos el algoritmo de preorder para recorrer el arbol y obtener el alfabeto y sus codigos
    def get_codes_table(self):
        return self.preorder(self.root)

    def preorder(self, node, codes = '', codes_table = {}):
        # Si el nodo actual tiene un caracter entonces es una hoja
        # y podemos agregarlo al diccionario
        if node.char is not None:
            codes_table[node.char] = codes
            return codes_table
        
        codes_table = self.preorder(node.left, codes + '0', codes_table)
        codes_table = self.preorder(node.right, codes + '1', codes_table)

        return codes_table

# Obtiene dos arboles con menor probabilidad de la lista de arboles>
# Entrada: Una lista de arboles
# Salida: Indices a los dos arboles con menor probabilidad
# Complejidad: O(n) donde n es la cantidad de arboles en la lista
def min_probs(trees):
    min_trees = [float('inf'), float('inf')]
    min_tree_indexes = [None, None]

    # Encontrar los dos arboles con menor probabilidad
    for index, tree in enumerate(trees):
        if tree.root.prob < min_trees[0]:
            min_trees[0] = tree.root.prob
            min_tree_indexes[0] = index

    for index, tree in enumerate(trees): 
        # Aqui si el valor de la probabilidad es menor al previo menor
        # y no es el primer arbola ya elegido entonces lo agregamos.
        if tree.root.prob < min_trees[1] and index != min_tree_indexes[0]:
            min_trees[1] = tree.root.prob
            min_tree_indexes[1] = index

    return tuple(min_tree_indexes)

# Recibe dos arboles y los une
# Entrada: Dos arboles
# Salida: Un arbol con los dos arboles de entrada fusionados
def merge_trees(tree1, tree2):
    # Calcular la nueva probabilidad
    merged_probability = tree1.root.prob + tree2.root.prob

    # Crear el nodo ya asignar las etiquetas
    new_root_node = Node(None, merged_probability)

    # Unir los nodos raiz y crear el nuevo arbol
    if tree1.root.prob <= tree2.root.prob:
        new_root_node.left = tree1.root
        new_root_node.right = tree2.root
    else:
        new_root_node.left = tree2.root
        new_root_node.right = tree1.root

    merged_tree = Tree(new_root_node)

    return merged_tree

# Función que genera el arbol de huffman para un alfabeto y sus probabilidades
# Entrada: Una lista de caracteres y una lista de probabilidades
# Salida: Un arbol de huffman
# Complejidad: O(n^2)
def create_huffman_tree(alphabet, probabilities):
    # Crear la lista con los arboles para cada caracter
    trees = []
    for i in range(len(alphabet)):
        node = Node(alphabet[i], probabilities[i])
        trees.append(Tree(node))

    # Si la lista sigue teniendo arboles por unir hay que elegir los dos arboles
    # con menor probabilidad y unirlos

    while len(trees) > 1:
        # Retorna una tupla con los indices de los arboles con menor 
        # probabilidad
        min_tree_indexes = min_probs(trees)

        # Obtener los dos arboles de la lista, unirlos y eliminarlos de la lista
        tree1 = trees.pop(min_tree_indexes[0])
        if min_tree_indexes[0] < min_tree_indexes[1]:
            tree2 = trees.pop(min_tree_indexes[1] - 1)
        else:
            tree2 = trees.pop(min_tree_indexes[1])
        
        # Unir los arboles 
        merged_tree = merge_trees(tree1, tree2)
        trees.append(merged_tree)
    
    # Retornar el ultimo arbol que resulte
    return trees[0]

# Codifica un texto a binario
# Entrada: Un texto y un arbol de huffman valido para ese texto
# Salida: Un texto en binario representando el texto de entrada
# Complejidad: O(n) donde n es la cantidad de caracteres en el texto
def encode(text, huffman_tree):
    # Obtenenmos el diccionario con los codigos de cada caracter
    codes_table = huffman_tree.get_codes_table()

    # Codificar el texto, recorriendo cada caracter y obteniendo su codigo respectivo
    binary_text = ''
    for character in text:
        if character in codes_table:
            binary_text += codes_table[character]
        else:
            raise Exception(f'El caracter {character} no esta en el alfabeto')
    
    return binary_text

# Decodifica un texto binario a su texto original en base a un arbol de huffman
# Entrada: Un texto binario y un arbol de huffman valido para ese texto
# Salida: El texto original
# Complejidad: O(n) donde n es la cantidad de bits en el texto binario
def decode(binary_text, huffman_tree):
    node = huffman_tree.root
    text = ''

    # Para decodificar el texto, recorremos cada bit del texto binario
    # y dependiendo de si es un 0 o un 1, nos movemos a la izquierda o derecha respectivamente
    # hasta llegar a una hoja, en cuyo caso agregamos el caracter al texto y volvemos a la raiz
    for bit in binary_text:
        if bit == '0':
            node = node.left
        elif bit == '1':
            node = node.right
        else:
            raise Exception(f'El formato es invalido')
        
        if node.char != None:
            text += node.char
            node = huffman_tree.root # Volver a la raiz

    return text

# Calcula la probabilidad de cada caracter en el texto
# Entrada: Un texto
# Salida: Una lista con las probabilidades de cada caracter
# Complejidad: O(n)
def calculate_character_probabilities(text):
    char_probs = {}
    probabilities = []
    total = len(text)

    # Contar las veces que aparece cada caracter
    for char in text:
        if char in char_probs:
            char_probs[char] += 1
        else:
            char_probs[char] = 1

    # Calcular la probabilidad de cada caracter
    for char in char_probs:
        probabilities.append(round(char_probs[char] / total, 2))
    
    return probabilities

# Obtiene los caracteres unicos en el texto
# Entrada: Un texto
# Salida: Una lista con los caracteres unicos en el texto
# Complejidad: O(n)
def get_unique_chars(text):
    seen = set()
    unique_chars = []

    # Para cada caracter en el texto, si no esta en el conjunto de caracteres entonces lo agregamos al conjunto de caracteres y a la lista de caracteres unicos
    for char in text:
        if char not in seen:
            unique_chars.append(char)
            seen.add(char)
    return unique_chars

# Lee un archivo y lo retorna como texto
def read_file(file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as file:
        text = file.read()

    return text

# Guarda un texto binario en un archivo
def save_binary_to_file(binaryText, file_path):
    with open(os.path.join(os.path.dirname(__file__), file_path), 'w') as file:
        file.write(binaryText)

def main():
    file_name = 'instrucciones_para_subir_una_escalera.txt'

    # Leer el archivo y convertirlo a mayusculas
    text = read_file(file_name)

    # Obtener el alfabeto
    alphabet = get_unique_chars(text)

    print("Codificando archivo a binario...")

    # Calcular probabilidades de cada caracter y ordenarlo en conjunto con el alfabeto
    probabilities = calculate_character_probabilities(text)
    huffman_tree = create_huffman_tree(alphabet, probabilities)
    binary_text = encode(text, huffman_tree)
    save_binary_to_file(binary_text, 'binario.txt')
    print("Archivo guardado en binario.txt")
    print("Tabla de codigos:", huffman_tree.get_codes_table())

    # NOTA: Para la parte de codificar y decodificar lo ingresado por el usuario es diferente al archivo puesto que
    # el archivo fue generado en base al alfabeto y probabilidades del texto. EN el caso siguiente se usa el alfabeto
    # completo con numeros y simbolos para que se pueda codificar cualquier texto que ingrese el usuario.

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,;:?!-()\|/_{}[]<>*^%$#@&+~=`"\''
    probabilities = calculate_character_probabilities(alphabet)
    huffman_tree = create_huffman_tree(alphabet, probabilities)
    print("\nDeseas codificar o decodificar un texto?")
    print("1. Codificar")
    print("2. Decodificar")
    print("3. Salir")

    option = int(input("Opcion: "))
    while option != 3:
        os.system('cls')
        if option == 1:
            text = input("Ingresa el texto a codificar: ")
            binary_text = encode(text, huffman_tree)
            print("Texto codificado:", binary_text)
        elif option == 2:
            binary_text = input("Ingresa el texto a decodificar: ")
            text = decode(binary_text, huffman_tree)
            print("Texto decodificado:", text)
        else:
            print("Opcion invalida")
        
        print("Deseas codificar o decodificar un texto?")
        print("1. Codificar")
        print("2. Decodificar")
        print("3. Salir")

        option = int(input("Opcion: "))
    os.system('cls')

if __name__ == '__main__':
    main()