def gcd(n, m):
    if (m == 0):
        return n
    elif m >= 1:
        return gcd(m, n % m)

    return

def main():
    print("gcd(60, 24) =", gcd(60, 24))
    print("gcd(126, 93) =", gcd(126, 93))
    print("gcd(45, 20) =", gcd(45, 20))

if __name__ == '__main__':
    main()