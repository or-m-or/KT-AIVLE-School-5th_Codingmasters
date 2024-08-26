'''
Type : 
'''


def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1
    return factors


def solution(p, n):
    factors = prime_factors(p)
    zeros = float('inf')

    for factor, power in factors.items():
        count = 0
        power_n = n
        while power_n > 0:
            power_n //= factor
            count += power_n
        zeros = min(zeros, count // power)

    return zeros


if __name__ == "__main__":
    p, n = map(int, input().split())
    print(solution(p, n))
