import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return (self.x, self.y)

class Segment:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def show(self):
        return [self.A.x, self.A.y, self.B.x, self.B.y]

class Triangle:
    def __init__(self, puntos):
        self.puntos = puntos
        s1 = Segment(puntos[0], puntos[1])
        s2 = Segment(puntos[1], puntos[2])
        s3 = Segment(puntos[2], puntos[0])
        self.sides = [s1, s2, s3]

def equal_segments(seg_1, seg_2):
    point1_seg1 = (seg_1.A.x, seg_1.A.y)
    point2_seg1 = (seg_1.B.x, seg_1.B.y)
    point1_seg2 = (seg_2.A.x, seg_2.A.y)
    point2_seg2 = (seg_2.B.x, seg_2.B.y)

    # Revisar si los segmentos son iguales
    if point1_seg1 == point1_seg2 and point2_seg1 == point2_seg2:
        return True

    if point1_seg1 == point2_seg2 and point2_seg1 == point1_seg2:
        return True

    return False

def unique_segments(triangles):
    segments = []
    for triangle in triangles:
        segments += triangle.sides

    different_segments = [False for i in range(len(segments))]

    for i in range(len(segments) - 1):
        for j in range(i + 1, len(segments)):
            # Si los segments son iguales, removerlos
            if equal_segments(segments[i], segments[j]):
                different_segments[i] = True
                different_segments[j] = True

    # Obtener todos los segments en false
    different_segments = [
        segments[i] for i in range(len(different_segments))
        if different_segments[i] == False
    ]

    # Imprimir todos los segments diferentes
    print("segments diferentes:")
    for segmento in different_segments:
        print(segmento.show())

    return different_segments

def main():
    triangles = [
        Triangle((Point(2.5, -6), Point(-7.5, 6), Point(2, 2))),
        Triangle((Point(2.5, 0), Point(2, 2), Point(7.5, -1))),
        Triangle((Point(2.5, -6), Point(2.5, 0), Point(7.5, -1))),
    ]

    segments = unique_segments(triangles)

    # Graficar los segments
    plt.title("segments únicos")
    for segment in segments:
        x_values_seg = [segment.A.x, segment.B.x]
        y_values_seg = [segment.A.y, segment.B.y]

        plt.plot(x_values_seg, y_values_seg, 'ro', linestyle="--", color="red")
    plt.show()

if __name__ == "__main__":
    main()