# Función recursiva que determina si un número es primo o no
# Entrada: number, entero positivo y el caso base que en este caso es 2.
# Salida: True si number es primo, False en otro caso.
# Complejidad: O(n), donde n es el número de veces que se llama a la función.
def is_prime(number, i = 2):
    # Si i es igual al numero inicial, entonces number es primo.
    if (number == i):
        return True

    # SI es 1 o 0, entonces no es primo.
    if (number == 0 or number == 1):
        return False

    # Si el numero es divisible entre i, entonces no es primo.
    if (number % i == 0):
        return False

    i += 1 # Incrementamos i para probar la siguiente división.
    return is_prime(number, i)

def main():
    # Prueba 1: 6 no es primo
    print("Prueba con 6:", is_prime(6))

    # Prueba 2: 5 es primo
    print("Prueba con 5:", is_prime(5))

    # Prueba 3: 1 no es primo
    print("Prueba con 1:", is_prime(1))

    # Prueba 4: 2 es primo
    print("Prueba con 1:", is_prime(2))

    # Prueba 5: 424 no es primo
    print("Prueba con 1:", is_prime(424))

if __name__ == "__main__":
    main()