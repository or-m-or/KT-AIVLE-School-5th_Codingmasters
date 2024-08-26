'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def is_good_array(n, arr):
    # 숫자의 첫 번째와 두 번째 위치를 저장하는 딕셔너리
    positions = {}

    # 배열을 순회하면서 각 숫자의 첫 번째와 두 번째 위치를 찾음
    for index, value in enumerate(arr, 1):  # 1부터 인덱싱
        if value in positions:
            positions[value].append(index)
        else:
            positions[value] = [index]

    # 배열의 전체 범위를 계산
    max_index = 2 * n

    # 모든 숫자에 대해 조건을 검사
    for pos in positions.values():
        i, p = pos  # 첫 번째와 두 번째 위치
        # i와 p 사이의 숫자들 (구간 A)
        set_A = set(arr[i:p-1])
        # p 이후의 모든 숫자들 (구간 B)
        set_B = set(arr[p:max_index])

        # 구간 A와 구간 B가 겹치면 "좋은 배열"이 아님
        if set_A & set_B:
            return "NO"

    return "YES"


if __name__ == "__main__":
    N = int(readline().strip())
    array = list(map(int, readline().split()))

    write(is_good_array(N, array)+'\n')
