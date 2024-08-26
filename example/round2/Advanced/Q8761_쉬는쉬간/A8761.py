def derangement_count(n):
    MOD = 998244353

    if n == 0:
        return 1
    elif n == 1:
        return 0

    D = [0] * (n + 1)
    D[0] = 1
    D[1] = 0

    for i in range(2, n + 1):
        D[i] = (i - 1) * (D[i - 1] + D[i - 2]) % MOD

    return D[n]

if __name__ == '__main__':
    N = int(input())
    print(derangement_count(N))
