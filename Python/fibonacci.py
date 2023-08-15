def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1

    return fibonacci(n-1) + fibonacci(n-2)

def main():
    # Pruebas
    print("Fibonacci de 10:", fibonacci(10))
    print("Fibonacci de 20:", fibonacci(20))
    print("Fibonacci de 30:", fibonacci(30))
    print("Fibonacci de 40:", fibonacci(40))

if __name__ == '__main__':
    main()