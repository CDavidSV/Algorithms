import matplotlib.pyplot as plt
import math

# Calcula a, b, c de la ecuacion de la recta que pasa por los puntos seg[0] y seg[1]
def calculate_equation(seg):
    a = seg[1][1] - seg[0][1]
    b = seg[0][0] - seg[1][0]
    c = a * seg[0][0] + b * seg[0][1]

    return a, b, c

def isInSegment(seg, point):
    # Calculate vector for segment and point
    seg_vec = [seg[1][0] - seg[0][0], seg[1][1] - seg[0][1]]
    point_vec = [point[0] - seg[0][0], point[1] - seg[0][1]]

    # Calculate the cross product
    cross_product = point_vec[1] * seg_vec[0] - point_vec[0] * seg_vec[1]
    
    # If the cross product isn't zero, the point doesn't lie on the line
    if abs(cross_product) != 0:
        return False

    # Calculate the dot product
    dot_product = point_vec[0] * seg_vec[0] + point_vec[1] * seg_vec[1]
    
    # Check that the point lies within the segment
    if dot_product < 0:
        return False
    
    # Check if the point lies within the segment and not on the extended line
    segment_length_squared = seg_vec[0]**2 + seg_vec[1]**2
    if dot_product > segment_length_squared:
        return False

    return True

def intersect(seg_1, seg_2):
    # Obtenemos las ecuaciones de los segmentos de recta
    a_1, b_1, c_1 = calculate_equation(seg_1)
    a_2, b_2, c_2 = calculate_equation(seg_2)

    # Calculamos el determinante
    d = a_1 * b_2 - a_2 * b_1

    # Si el determinante es 0, las rectas son paralelas
    if d == 0:
        return False

    # Calcular en donde se intersectan las rectas
    x = (b_2 * c_1 - b_1 * c_2) / d
    y = (a_1 * c_2 - a_2 * c_1) / d

    # Verificar si el punto de interseccion esta en los segmentos
    if not isInSegment(seg_1, (x, y)) or not isInSegment(seg_2, (x, y)):
        return False
    
    # Graficar los segmentos y el punto de interseccion
    x_values_seg_1 = [seg_1[0][0], seg_1[1][0]]
    y_values_seg_1 = [seg_1[0][1], seg_1[1][1]]
    x_values_seg_2 = [seg_2[0][0], seg_2[1][0]]
    y_values_seg_2 = [seg_2[0][1], seg_2[1][1]]

    plt.plot(x_values_seg_1, y_values_seg_1, 'ro', linestyle="--", color="red")
    plt.plot(x_values_seg_2, y_values_seg_2, 'bo', linestyle="--", color="green")

    # Graficar el punto de interseccion
    plt.plot(x, y, 'ro', color="blue")

    plt.text(x + 0.030 , y + 0.030, "({}, {}) Intersección".format(round(x, 2), round(y, 2)))
    plt.show()

    return d

def main():
    seg_1 = ((0, 0), (1, 1))
    seg_2 = ((0, 1), (0, 0))

    print(intersect(seg_1, seg_2))

if __name__ == "__main__":
    main()