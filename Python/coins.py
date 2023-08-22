def recursive_coin_change(C, n, K):
    if K == 0: return 1
    if n <= 0 or K < 0: return 0

    return recursive_coin_change(C, n, K - C[n - 1]) + recursive_coin_change(C, n - 1, K) 

def coin_change_memo(C, n, K, T):
    if K == 0: 
        T[n][K] = 1
        return T[n][K]
    
    if n <= 0 or K < 0: 
        return 0
    
    if T[n][K] != None: return T[n][K]

    T[n][K] = coin_change_memo(C, n, K - C[n - 1], T) + coin_change_memo(C, n - 1, K, T)
    return T[n][K]

def main():
    C = [1,2,5,10]
    n = len(C)
    K = 5
    T = [[None for i in range(K + 1)] for j in range(n + 1)]
    T[0][0] = 1

    print("Caso recursive con ecuación de Bellman: ")
    print(recursive_coin_change(C, n, K))
    print("")

    print("Caso memoization con ecuación de Bellman: ")
    print(coin_change_memo(C, n, K, T))



if __name__ == '__main__':
    main()