#include <iostream>
#include <vector>
#include <string>

/*
Función que imprime el resultado de la función stringMatching.
Entrada: Un vector de vectores de enteros que contiene los indices de las coincidencias.
Regresa: Nada.
*/
void printResult(std::vector<std::vector<int>> inputVector) {
    // Si el vector esta vacio entonces no se encontraron coincidencias.
    if (inputVector.empty()) {
        std::cout << "No se encontradon coincidencias" << std::endl;
    }

    // Imprimimos cada coincidencia.
    for (int i = 0; i < inputVector.size(); i++) {
        std::cout << "Coincidencia " << i + 1 << ": ";
        for (int j = 0; j < inputVector.at(i).size(); j++) {
            std::cout << inputVector.at(i).at(j) << " ";
        }
        std::cout << std::endl;
    }
}

/*
Función que busca todas las coincidencias de un string dentro de otro y regresa los indices de las coincidencias.
Entrada: Dos strings, el primero es el string original y el segundo es el string a buscar.
Regresa: Un vector de vectores de enteros que contiene los indices de las coincidencias.
Complejidad: O(n)
*/
std::vector<std::vector<int>> stringMatching(std::string inputString, std::string matchString) {
    // Vector que contiene los indices de las coincidencias.
    std::vector<std::vector<int>> matchIndexes;

    int matchStringSize = matchString.length();
    int inputStringSize = inputString.length();

    int matchStringIndex = 0;
    for (int i = 0; i < inputStringSize; i++) {
        if (matchStringIndex >= matchString.size()) { // Si el indice del string a buscar es mayor a su tamaño entonces se reinicia.
            matchStringIndex = 0;
        }

        // Si el caracter actual del string a buscar no coincide con el caracter actual del string original entonces reiniciamos el indice del string a buscar.
        if (matchString.at(matchStringIndex) != inputString.at(i)) {
            matchStringIndex = 0;
            if (!matchIndexes.empty() && matchIndexes.back().size() != matchStringSize) { // Si el ultimo vector del vector de vectores no esta completo entonces lo eliminamos.
                matchIndexes.pop_back();
            }

            continue;
        }

        // Si el vector de vectores esta vacio o el ultimo vector del vector de vectores esta completo entonces creamos un nuevo vector.
        if (matchIndexes.empty() || matchIndexes.back().size() == matchStringSize) {
            std::vector<int> newIndexVector;
            newIndexVector.push_back(i);

            matchIndexes.push_back(newIndexVector);
        } else {
            matchIndexes.back().push_back(i);
        }

        matchStringIndex++;
    }

    // Asegurarse de que el ultimo vector del vector de vectores este completo.
    if (!matchIndexes.empty() && matchIndexes.back().size() != matchStringSize) {
        matchIndexes.pop_back();
    }

    return matchIndexes;
}

int main() {
    std::vector<std::vector<int>> result;
    std::string original;
    std::string match;

    // Test 1
    original = "Prueba 1 con la palabra string";
    match = "string";
    result = stringMatching(original, match);
    std::cout << "Test 1:" << std::endl;
    printResult(result);

    // Test 2
    original = "abababab";
    match = "aba";
    result = stringMatching(original, match);
    std::cout << "\nTest 2:" << std::endl;
    printResult(result);

    // Test 3
    original = "Mississippi";
    match = "iss";
    result = stringMatching(original, match);
    std::cout << "\nTest 3:" << std::endl;
    printResult(result);

    // Test 4
    original = "aaaaaa";
    match = "aa";
    result = stringMatching(original, match);
    std::cout << "\nTest 4:" << std::endl;
    printResult(result);

    return 0;
}