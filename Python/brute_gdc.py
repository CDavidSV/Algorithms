def gdc(n, m):
    if (n == 0 and m == 0): return None
    if (n == 0): return m
    if (m == 0): return n

    minValue = min(n, m)

    while (minValue > 0):
        if (n % minValue == 0 and m % minValue == 0): return minValue
        minValue -= 1

def main():
    print("gdc(60, 24) =", gdc(60, 24))
    print("gdc(126, 93) =", gdc(126, 93))
    print("gdc(45, 20) =", gdc(45, 20))

if __name__ == '__main__':
    main()