'''
Type : 
'''
from math import factorial


def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


if __name__ == "__main__":
    N, K = map(int, input().split())

    # 수익을 얻기 위해 주식 가격이 오르는 일수 계산
    x = (K + 100 * N) // 200

    # x가 정수이며 0 ≤ x ≤ N 조건을 만족하는지 확인
    if (K + 100 * N) % 200 == 0 and 0 <= x <= N:
        # 경우의 수 계산
        result = combinations(N, x)
    else:
        result = 0

    print(result)
