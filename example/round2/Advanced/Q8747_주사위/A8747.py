MOD = 1000000007

def matrix_mult(A, B, size=4):
    return [[sum(A[i][k] * B[k][j] for k in range(size)) % MOD for j in range(size)] for i in range(size)]

def matrix_pow(mat, exp, size=4):
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    base = mat

    while exp > 0:
        if exp % 2 == 1:
            result = matrix_mult(result, base, size)
        base = matrix_mult(base, base, size)
        exp //= 2

    return result

def count_ways(N):
    if N <= 4:
        return [1, 2, 4, 8][N - 1]

    # Transition matrix
    T = [
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
    ]

    # Initial state vector (dp[4], dp[3], dp[2], dp[1])
    F = [8, 4, 2, 1]

    T_exp = matrix_pow(T, N - 4)

    result = sum(T_exp[0][i] * F[i] for i in range(4)) % MOD
    return result


if __name__=="__main__":
    N = int(input())
    print(count_ways(N))
