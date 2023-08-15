def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    print("Factorial de 5:", factorial(5))
    print("Factorial de 10:", factorial(10))
    print("Factorial de 20:", factorial(20))
    print("Factorial de 50:", factorial(50))

if __name__ == "__main__":
    main()