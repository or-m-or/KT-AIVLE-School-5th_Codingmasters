MOD = 1000000007

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % MOD
    return result

def power(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % MOD
        base = (base * base) % MOD
        exponent //= 2
    return result

if __name__ == "__main__":
    N = int(input())
    permutations = factorial(N) 
    cycles = (permutations - power(2, N - 1) + MOD) % MOD 
    print(cycles)