from collections import deque, defaultdict


def bfs(N, graph, S1, D1, S2, D2):
    # 초기 상태: (컨테이너1 위치, 컨테이너2 위치, 이동 횟수)
    queue = deque([(S1, S2, 0)])
    visited = set((S1, S2))

    while queue:
        pos1, pos2, moves = queue.popleft()

        # 두 컨테이너가 각각 목적지에 도달했는지 확인
        if pos1 == D1 and pos2 == D2:
            return moves

        # 컨테이너 1을 이동시키는 경우
        for neighbor in graph[pos1]:
            if neighbor != pos2 and (neighbor, pos2) not in visited:
                visited.add((neighbor, pos2))
                queue.append((neighbor, pos2, moves + 1))

        # 컨테이너 2를 이동시키는 경우
        for neighbor in graph[pos2]:
            if neighbor != pos1 and (pos1, neighbor) not in visited:
                visited.add((pos1, neighbor))
                queue.append((pos1, neighbor, moves + 1))

    # 두 컨테이너를 주어진 위치로 재배치할 수 없는 경우
    return -1


def solution(N, S1, D1, S2, D2, roads):
    # 그래프 구성
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    # BFS 탐색을 통해 최소 이동 횟수 계산
    return bfs(N, graph, S1, D1, S2, D2)


if __name__ == "__main__":
    N, M = map(int, input().split())
    S1, D1, S2, D2 = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(M)]
    print(solution(N, S1, D1, S2, D2, roads))
