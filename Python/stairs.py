def stairs_memo(n, a = 1, b = 2):
    if n <= 0: return 0
    if n == 1: return a
    if n == 2: return b

    return stairs_memo(n-1, b, a+b)

def stairs_tabu(n):
    stairs = [0 for i in range(0, n+1)]

    if n == 0: return 0
    stairs[1] = 1
    stairs[2] = 2

    for i in range(3, n+1):
        stairs[i] = stairs[i-1] + stairs[i-2]

    return stairs[n]

def main():
    print("stairs_memo(3) =", stairs_memo(3))
    print("stairs_memo(7) =",stairs_memo(7))
    print("stairs_memo(12) =",stairs_memo(12))

    print("stairs_tabu(7) =", stairs_tabu(7))
    print("stairs_tabu(34) =", stairs_tabu(34))
    print("stairs_tabu(12) =", stairs_tabu(12))

if __name__ == '__main__':
    main()