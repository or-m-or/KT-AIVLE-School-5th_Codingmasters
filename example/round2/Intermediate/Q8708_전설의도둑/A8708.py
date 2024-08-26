'''
Type : BFS
'''
from collections import deque
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def min_warp(K, N):
    # BFS에 필요한 큐와 방문 체크 배열
    queue = deque([(K, 0)])  # (현재 위치, 현재까지 워프 횟수)
    visited = [False] * 100001  # 100000까지의 위치를 방문했는지 체크
    visited[K] = True

    while queue:
        current, warps = queue.popleft()

        # 목표 위치에 도달했을 경우
        if current == N:
            return warps

        # 워프를 통해 갈 수 있는 다음 위치들
        next_positions = [current + 3, current - 1, current * 2]

        for next_pos in next_positions:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, warps + 1))

    return -1


if __name__ == "__main__":
    K, N = map(int, readline().split())
    write(f'{min_warp(K, N)}\n')
