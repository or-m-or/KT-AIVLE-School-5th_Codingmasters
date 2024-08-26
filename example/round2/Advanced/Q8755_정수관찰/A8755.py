from math import gcd
from functools import reduce
from itertools import combinations


def lcm(a, b):
    return a * b // gcd(a, b)


def count_multiples_below(limit, x):
    return (limit + 1) // x


def solution(N, a):
    limit = 10 ** 9
    total_count = 0

    # 1. 모든 집합의 크기 더하기 (단일 집합)
    for i in range(1, N + 1):
        for comb in combinations(a, i):
            lcm_val = reduce(lcm, comb)
            count = count_multiples_below(limit, lcm_val)
            if i % 2 == 1:  # odd length combinations
                total_count += count
            else:  # even length combinations
                total_count -= count

    return total_count


if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split()))
    result = solution(N, a)
    print(result)
