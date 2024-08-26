from fractions import Fraction
from math import gcd


def solve_monyubyeong(N, K, A, B, C, X):
    total = A + B + C
    p = Fraction(A, total)
    q = Fraction(B, total)
    r = Fraction(C, total)

    dp = [[Fraction(0) for _ in range(N + 1)] for _ in range(X + 1)]
    dp[0][K] = Fraction(1)

    for t in range(1, X + 1):
        for i in range(1, N + 1):
            if i > 1:
                dp[t][i] += dp[t - 1][i - 1] * p
            dp[t][i] += dp[t - 1][i] * r
            if i < N:
                dp[t][i] += dp[t - 1][i + 1] * q

    wake_prob = Fraction(0)
    for t in range(1, X + 1):
        if dp[t - 1][1] * q > 0:
            wake_prob += dp[t - 1][1] * q
        if dp[t - 1][N] * p > 0:
            wake_prob += dp[t - 1][N] * p

    final_probs = [dp[X][i] for i in range(1, N + 1)]

    def to_simplest_fraction(frac):
        numerator = frac.numerator
        denominator = frac.denominator
        common_divisor = gcd(numerator, denominator)
        numerator //= common_divisor
        denominator //= common_divisor
        if denominator == 1:
            return f"{numerator}/1"
        else:
            return f"{numerator}/{denominator}"

    result_floors = [to_simplest_fraction(final_probs[i]) for i in range(N)]
    result_wake = to_simplest_fraction(wake_prob)

    print(' '.join(result_floors))
    print(result_wake)


if __name__ == "__main__":
    N, K, A, B, C, X = map(int, input().split())
    solve_monyubyeong(N, K, A, B, C, X)


# 예제 출력 2 잘린부분
'''
19992/390625 46668/390625 74256/390625 86514/390625 14856/78125 46927/390625 21648/390625 278/15625
2678/78125
'''