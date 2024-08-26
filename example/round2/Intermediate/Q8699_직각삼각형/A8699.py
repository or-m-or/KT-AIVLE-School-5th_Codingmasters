'''
Type : 
'''
import sys
import math

readline = sys.stdin.readline
write = sys.stdout.write


def find_max_right_triangles(N):
    max_count = 0
    best_perimeter = 0

    # 둘레 P에 대해 모든 가능한 값을 검사
    for P in range(12, N + 1):
        count = 0

        # a와 b를 선택 (a <= b, a + b < c)
        for a in range(1, P // 3):
            for b in range(a, (P - a) // 2):
                c = P - a - b
                if a**2 + b**2 == c**2:  # 피타고라스 정리 확인
                    count += 1

        # 최대 직각삼각형의 수를 갱신
        if count > max_count:
            max_count = count
            best_perimeter = P

    return best_perimeter, max_count


def solution(N):
    perimeter_count = {}
    for a in range(1, N // 3 + 1):  # a : 최대 N/3
        for b in range(a, (N - a) // 2 + 1):  # b : a 이상, (N-a)/2 이하
            c = math.sqrt(a**2 + b**2)
            if c.is_integer():
                c = int(c)
                p = a + b + c
                if p <= N:
                    if p in perimeter_count:
                        perimeter_count[p] += 1
                    else:
                        perimeter_count[p] = 1

    max_triangles = 0
    min_perimeter = None
    for p, count in perimeter_count.items():
        if count > max_triangles:
            max_triangles = count
            min_perimeter = p
        elif count == max_triangles:
            if min_perimeter is None or p < min_perimeter:
                min_perimeter = p

    return min_perimeter, max_triangles


if __name__ == "__main__":
    N = int(readline().strip())
    ans = solution(N)
    write(f'{ans[0]} {ans[1]}\n')
