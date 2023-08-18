def gdc(n, m):
    if (m == 0):
        return n
    elif m >= 1:
        return gdc(m, n % m)

    return

def main():
    print("gdc(60, 24) =", gdc(60, 24))
    print("gdc(126, 93) =", gdc(126, 93))
    print("gdc(45, 20) =", gdc(45, 20))

if __name__ == '__main__':
    main()