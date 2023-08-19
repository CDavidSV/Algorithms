def gcd(n, m):
    if (n == 0 and m == 0): return None
    if (n == 0): return m
    if (m == 0): return n

    minValue = min(n, m)

    while (minValue > 0):
        if (n % minValue == 0 and m % minValue == 0): return minValue
        minValue -= 1

def main():
    print("gcd(60, 24) =", gcd(60, 24))
    print("gcd(126, 93) =", gcd(126, 93))
    print("gcd(45, 20) =", gcd(45, 20))

if __name__ == '__main__':
    main()