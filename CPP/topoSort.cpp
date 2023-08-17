#include <iostream>
#include <vector>
#include <algorithm>

/*
Función que permite imprimir un vector.
Entrada: vector de enteros.
Salida: void.
*/
void printVector(std::vector<int> inputVector) {
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
	std::vector<int> nodeEdges(adjList.size(), 0);
	for (const auto& neighbors : adjList) {
		for (int neighbor : neighbors) {
			if (neighbor >= 0 && static_cast<std::size_t>(neighbor) < nodeEdges.size()) {
				nodeEdges[neighbor]++;
			}
		}
	}

	int node = -1;
	for (int i = 0; i < nodeEdges.size(); i++) {
		if (nodeEdges[i] == 0 && !std::count(exclude.begin(), exclude.end(), i)) {
			node = i;
			break;
		}
	}

	return node;
}

/*
Función que permite ordenar topológicamente un grafo.
Entrada: lista de adyacencia.
Salida: vector con el orden topológico del grafo.
Complejidad: O(V + E).
*/
std::vector<int> topoSort(std::vector<std::vector<int>> adjList) {
	std::vector<int> L;
	std::vector<int> visited;
	int adjListSIze = adjList.size();

	int nodeWithNoIncomingEdges = findNodeWithNoIncomingEdges(adjList, visited);
	while (nodeWithNoIncomingEdges > -1) {
		L.push_back(nodeWithNoIncomingEdges);

		adjList[nodeWithNoIncomingEdges] = {};
		visited.push_back(nodeWithNoIncomingEdges);
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
	std::vector<std::vector<int>> adjListTest = {
		{1, 2},
		{4, 6},
		{5},
		{0, 1, 2, 5, 6},
		{},
		{},
		{4}
	};
	
	printVector(topoSort(adjListTest));

	return 0;
}