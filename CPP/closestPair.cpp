#include <iostream>
#include <vector>
#include <utility>
#include <cmath>

/*
Calcula la distancia entre dos puntos por medio de teorema de pitágoras.
Entrada: Dos pares que contienes los valores x,y de ambos puntos a calcular la distancia.
Regresa: El resultado del cálculo de la distancia.
*/
double calculatePointDistance(std::pair<double, double> point1, std::pair<double, double> point2) {
    return std::sqrt(std::pow(point2.first - point1.first, 2) + std::pow(point2.second - point1.second, 2));
}

/*
De un vector de pares con cordenadas x,y calcula los dos puntos mas cernanos.
Entrada: Un vector de pares, cada uno representando el punto x,y de un punto.
Regresa: Vector con ambos indices de los puntos más cercanos y su distancia.
Complejidad: O(n^2)
*/
std::vector<double> closestPair(std::vector<std::pair<double, double>>& points) {

    // Calculamos la distancia entre los primeros dos puntos en el vector.
    double currentMin = calculatePointDistance(points.at(0), points.at(2));

    // Asignamos los indices iniciales
    double point1MinIndex = 0;
    double point2MinIndex = 1;

    // Recorremos la lista y vamos comparando cada posible combinación de puntos.
    for (double point1 = 1; point1 < points.size(); point1++) {
        for (double point2 = point1 + 1; point2 < points.size(); point2++) {

            // Calculamos la nueva distancia.
            double pointDistance = calculatePointDistance(points.at(point1), points.at(point2));

            // Si la distancia calculada es menor a la anterios entonces la cambiamos y modificamos los indices.
            if (pointDistance < currentMin) {
                currentMin = pointDistance;
                point1MinIndex = point1;
                point2MinIndex = point2;
            }
        }
    }

    // Retornamos los indices y la distancia en un vector.
    // TODO: Seria mejor una tupla.
    std::vector<double> result = { point1MinIndex, point2MinIndex, currentMin };

    return result;
}

int main() {
    // Prueba 1
    std::vector<std::pair<double, double>> points1 = { {1, 2}, {3, 4}, {5, 6}, {7, 8}, {9, 10}, {11, 12} };
    std::vector<double> result1 = closestPair(points1);
    std::cout << "Prueba 1: Par de indices cercanos: " << result1.at(0) << " " << result1.at(1) << std::endl;
    std::cout << "Distancia: " << result1.at(2) << std::endl;

    // Prueba 2
    std::vector<std::pair<double, double>> points2 = { {0, 0}, {1, 1}, {2, 2}, {3, 3}, {4, 4} };
    std::vector<double> result2 = closestPair(points2);
    std::cout << "Prueba 2: Par de indices cercanos: " << result2.at(0) << " " << result2.at(1) << std::endl;
    std::cout << "Distancia: " << result2.at(2) << std::endl;

    // Prueba 3
    std::vector<std::pair<double, double>> points3 = { {-1, -1}, {1, 1}, {-2, 2}, {3, 3}, {-4, 4}, {5, -5} };
    std::vector<double> result3 = closestPair(points3);
    std::cout << "Prueba 3: Par de indices cercanos: " << result3.at(0) << " " << result3.at(1) << std::endl;
    std::cout << "Distancia: " << result3.at(2) << std::endl;

    // Prueba 4
    std::vector<std::pair<double, double>> points4 = { {-10, 5}, {3, -7}, {8, 12}, {-5, 10}, {0, 0} };
    std::vector<double> result4 = closestPair(points4);
    std::cout << "Prueba 4: Par de indices cercanos: " << result4.at(0) << " " << result4.at(1) << std::endl;
    std::cout << "Distancia: " << result4.at(2) << std::endl;

    // Prueba 5
    std::vector<std::pair<double, double>> points5 = { {1, 1}, {2, 2}, {3, 3}, {4, 4}, {5, 5}, {6, 6} };
    std::vector<double> result5 = closestPair(points5);
    std::cout << "Prueba 5: Par de indices cercanos: " << result5.at(0) << " " << result5.at(1) << std::endl;
    std::cout << "Distancia: " << result5.at(2) << std::endl;

    return 0;
}