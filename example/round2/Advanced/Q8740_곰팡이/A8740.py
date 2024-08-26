'''
Type : 행렬 곱셈, 행렬 거듭제곱 -> 피보나치 수 계산
'''
MOD = 1000000007

def matrix_mult(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]

def matrix_pow(mat, exp):
    result = [[1, 0], [0, 1]]
    base = mat
    while exp > 0:
        if exp % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        exp //= 2
    return result

def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, n-1)
    return (result[0][0] + result[0][1]) % MOD

if __name__=="__main__":
    N = int(input().strip())
    print(fibo(N))
