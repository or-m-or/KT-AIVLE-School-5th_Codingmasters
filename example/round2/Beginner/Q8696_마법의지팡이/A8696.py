'''
Type : BFS
'''
import sys
from collections import deque

readline = sys.stdin.readline
write = sys.stdout.write


def min_count(n):
    # 입력된 숫자가 이미 1이면 필요한 연산은 0회입니다.
    if n == 1:
        return 0

    # 숫자와 해당 숫자에 도달하기까지의 연산 횟수를 저장하기 위한 큐
    queue = deque([(n, 0)])
    visited = set([n])  # 같은 숫자를 중복 방문하지 않기 위해 사용하는 집합

    while queue:
        current, steps = queue.popleft()

        # 가능한 변환 연산 적용
        if current % 2 == 0:
            next_num = current // 2
            if next_num == 1:
                return steps + 1  # 1에 도달하면 연산 횟수 반환
            if next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, steps + 1))

        if current % 3 == 0:
            next_num = (current // 3) * 2
            if next_num == 1:
                return steps + 1  # 1에 도달하면 연산 횟수 반환
            if next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, steps + 1))

        if current % 5 == 0:
            next_num = (current // 5) * 4
            if next_num == 1:
                return steps + 1  # 1에 도달하면 연산 횟수 반환
            if next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, steps + 1))

    # 큐를 다 소모했으나 1에 도달하지 못한 경우
    return -1


if __name__ == "__main__":
    N = int(readline())
    write(f'{min_count(N)}')
