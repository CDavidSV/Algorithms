# Este es un caso de un algorítmo de divide y vencerás, puesto que dividimos el exponente a la mitad en cada llamada recursiva.
# Esto lo hace más eficiente que el algorítmo de fuerza bruta, que va por cada número desde 1 hasta el exponente, lo que lo hace O(n)
# en vez de O(log n) como este algorítmo.

# Función recursiva que calcula la potencia de un número a^n.
# Entrada: Número n y potencia p.
# Salida: Potencia de n^p.
# Complejidad: O(log n), debido a que dividimos el exponente a la mitad en cada llamada recursiva.
def pow(n, p):
    # Casoso base cuando el exponente es 0 o 1.
    if p == 0: return 1
    if p == 1: return n

    # Dividimos el exponente a la mitad.
    p1 = p // 2
    p2 = p - p1

    # Llamada recursiva para calcular, por ejemplo, 2^5 = 2^2 * 2^3.
    return pow(n, p1) * pow(n, p2)

def main():
    print("2^4 =", pow(2, 4))
    print("2^5 =", pow(2, 5))
    print("6^31 =", pow(6, 31))
    print("4^10 =", pow(4, 10))
    print("3^13 =", pow(3, 13))

if __name__ == '__main__':
    main()