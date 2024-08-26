'''
Type : 
'''
import sys
from collections import deque, defaultdict

readline = sys.stdin.readline
write = sys.stdout.write
MOD = 1_000_000_007


def shortest_path_count(n, edges):
    # 그래프를 인접 리스트로 표현
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # 거리와 경로 수를 저장할 리스트 초기화
    dist = [float('inf')] * (n + 1)
    count = [0] * (n + 1)

    # BFS 초기 설정
    queue = deque([1])
    dist[1] = 0
    count[1] = 1

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            # 현재 방에서 이웃 방으로 이동하는 경우
            if dist[neighbor] > dist[current] + 1:
                dist[neighbor] = dist[current] + 1
                count[neighbor] = count[current]
                queue.append(neighbor)
            elif dist[neighbor] == dist[current] + 1:
                count[neighbor] = (count[neighbor] + count[current]) % MOD

    # n번 방까지의 최단 경로 수 반환
    return count[n]


if __name__ == "__main__":
    n, k = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(k)]
    write(f'{shortest_path_count(n, edges)}\n')
