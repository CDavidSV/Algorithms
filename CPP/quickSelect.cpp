#include <iostream>
#include <vector>
#include <utility>

// Función que permite intercambiar dos elementos de un vector.
void swap(std::vector<int>& inputVector, int index1, int index2) {
    // Asignamos el valor del primer elemento a una variable temporal.
	int temp = inputVector[index1];

    // Intercambiamos los valores de los elementos.
	inputVector[index1] = inputVector[index2];
	inputVector[index2] = temp;
}

/*
Función que desplaza un pivote a su posición correcta en un vector ordenado.
Entrada: vector de enteros, índice de inicio, índice de fin.
Salida: vector de enteros.
*/
std::pair<int, std::vector<int>> lomuto(std::vector<int> inputVector, int start, int end) {
	int s = start; // Indice del primer elemento.
	int pivot = inputVector[0]; // Asignamos el primer elemento como pivote.

	for (int i = start + 1; i < end; i++) { // Recorremos la parte seleccionada del vector.
		if (inputVector[i] < pivot) { // Si el valor en el indice actual es menor al pivote, entonces incrementamos el indice de s y lo intercambiamos con s.
			s++;
			swap(inputVector, s, i); // Interacambiamos los valores de los elementos.
		}
	}
	swap(inputVector, s, start); // Intercambamos el pivote con el valor en el indice s.

	return {s, inputVector}; // Retornamos un par que corresponde a s y el vector modificado.
}

/*
Función que permite encontrar el k-ésimo elemento más pequeño de un vector.
Entrada: vector de enteros, k.
Salida: k-ésimo elemento más pequeño del vector.
Complejidad: O(n) en promedio, O(n^2) en el peor de los casos.
*/
int quickSelect(std::vector<int> inputVector, int k) {
    // Calculamos el valor de s mediante el algoritmo de Lomuto.
	std::pair<int, std::vector<int>> lomutoResult = lomuto(inputVector, 0, inputVector.size());

    // Si el valor de s es igual a k, entonces retornamos el valor en el indice s que corresponde al k-ésimo elemento más pequeño.
	while (lomutoResult.first != k) {
		int start = 0;
		int end = inputVector.size();

        // Si el valor de s es menor a k, entonces buscamos el k-ésimo elemento más pequeño en la parte derecha del vector.
		if (lomutoResult.first < k) {
			start = lomutoResult.first + 1;
		} else { // Si el valor de s es mayor a k, entonces buscamos el k-ésimo elemento más pequeño en la parte izquierda del vector.
			end = lomutoResult.first;
		}
		lomutoResult = lomuto(lomutoResult.second, start, end); // Ejecutamos el algoritmo de Lomuto en base a la parte seleccionada del vector.
	}
	return lomutoResult.second[lomutoResult.first]; // Retornamos el elemento cuando s es igual a k.
}

int main() {
    int k;

    // Prueba 1
    k = 2;
    std::vector<int> A1 = {6, 1, 24, 4, 5, 7, 2, 8, 9};
    int result1 = quickSelect(A1, k);
    std::cout << "Prueba 1: " << result1 << std::endl;

    // Prueba 2
    k = 4;
    std::vector<int> A2 = {9, 8, 7, 6, 5, 4, 3, 2, 1};
    int result2 = quickSelect(A2, k);
    std::cout << "Prueba 2: " << result2 << std::endl;

    // Prueba 3
    k = 6;
    std::vector<int> A3 = {15, 12, 6, 20, 10, 9, 8, 4};
    int result3 = quickSelect(A3, k);
    std::cout << "Prueba 3: " << result3 << std::endl;

    // Prueba 4
    k = 1;
    std::vector<int> A4 = {100, 50, 25, 75, 150, 125, 175};
    int result4 = quickSelect(A4, k);
    std::cout << "Prueba 4: " << result4 << std::endl;

    return 0;
}