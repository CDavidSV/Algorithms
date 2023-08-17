#include <iostream>
#include <vector>
#include <algorithm>

/*
Función que permite imprimir un vector.
Entrada: vector de enteros.
Salida: void.
*/
void printVector(std::vector<int> inputVector) {
	if (inputVector.size() == 0) {
		std::cout << "El grafo es ciclico" << std::endl;
	}

	for (int i = 0; i < inputVector.size(); i++) {
		std::cout << inputVector[i] << " ";
	}
	std::cout << std::endl;
}

/*
Función que permite encontrar un nodo con aristas entrantes igual a cero.
Entrada: lista de adyacencia, vector de nodos excluidos.
Salida: nodo con aristas entrantes igual a cero.
*/
int findNodeWithNoIncomingEdges(std::vector<std::vector<int>> adjList, std::vector<int> exclude) {
	// Inicializamos un vector con el número de aristas entrantes de cada nodo.
	std::vector<int> nodeEdges(adjList.size(), 0);

	// Recorremos la lista de adyacencia para contar el número de aristas entrantes de cada nodo.
	for (const auto& neighbors : adjList) {
		for (int neighbor : neighbors) {
			if (neighbor >= 0 && static_cast<std::size_t>(neighbor) < nodeEdges.size()) {
				nodeEdges[neighbor]++; // Sumamos uno al número de aristas entrantes del nodo.
			}
		}
	}

	// Determinamos el nodo con aristas entrantes igual a cero.
	int node = -1;
	for (int i = 0; i < nodeEdges.size(); i++) {
		if (nodeEdges[i] == 0 && !std::count(exclude.begin(), exclude.end(), i)) {
			node = i;
			break;
		}
	}

	return node; // si es -1, no se encontró ningún nodo con aristas entrantes igual a cero.
}

/*
Función que permite ordenar topológicamente un grafo.
Entrada: lista de adyacencia.
Salida: vector con el orden topológico del grafo.
Complejidad: O(V + E).
*/
std::vector<int> topoSort(std::vector<std::vector<int>> adjList) {
	std::vector<int> L; // Vector que contendrá el orden topológico del grafo.
	std::vector<int> visited; // Vector que contendrá los nodos visitados.
	int adjListSIze = adjList.size();

	// Encontramos un nodo sin aristas entrantes.
	int nodeWithNoIncomingEdges = findNodeWithNoIncomingEdges(adjList, visited);
	while (nodeWithNoIncomingEdges > -1) { // Si no es menor a 0 es porque se encontró un nodo.
		L.push_back(nodeWithNoIncomingEdges); // Agregamos el nodo al vector ordenado.

		adjList[nodeWithNoIncomingEdges] = {}; // Eliminamos el nodo de la lista de adyacencia.
		visited.push_back(nodeWithNoIncomingEdges); // Agregamos el nodo a la lista de visitados.
		nodeWithNoIncomingEdges = findNodeWithNoIncomingEdges(adjList, visited);
	}

	if (L.size() != adjListSIze) {
		// El grafo es ciclico, puesto que el tamaño del vector ordenado no es el mismo a la lista de nodos.
		return {};
	}

	return L;
}

int main() {
	// Prueba 1
	std::vector<std::vector<int>> adjListTest1 = {
		{1, 2},
		{4, 6},
		{5},
		{0, 1, 2, 5, 6},
		{},
		{},
		{4}
	};

	std::cout << "Resultados de prueba 1: ";
	printVector(topoSort(adjListTest1));

	// Prueba 2
	std::vector<std::vector<int>> adjListTest2 = {
		{1, 2, 3},
		{4},
		{4, 5},
		{5},
		{},
		{}
	};

	std::cout << "Resultados de prueba 2: ";
	printVector(topoSort(adjListTest2));

	// Prueba 3
	std::vector<std::vector<int>> adjListTest3 = {
		{1, 2},
		{3},
		{},
		{2},
		{5},
		{4}
	};

	std::cout << "Resultados de prueba 3: ";
	printVector(topoSort(adjListTest3));

	return 0;
}