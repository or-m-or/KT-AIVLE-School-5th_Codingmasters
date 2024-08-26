'''
Type : Dijkstra
'''
import sys
import heapq

readline = sys.stdin.readline
write = sys.stdout.write


def dijkstra(N, edges, start, end):
    # 그래프 초기화
    graph = [[] for _ in range(N+1)]
    for U, V, T in edges:
        graph[U].append((V, T))

    INF = sys.maxsize
    distance = [INF] * (N+1)
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    # 우선순위 큐가 빌 때까지 순회
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # 현재 노드가 이미 처리된 적 있으면 무시
        if distance[current_node] < current_distance:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for adj, weight in graph[current_node]:
            cost = current_distance + weight

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[adj]:
                distance[adj] = cost
                heapq.heappush(pq, (cost, adj))

    return distance[end]


if __name__ == "__main__":
    N = int(readline())  # 버스 정류장 수
    M = int(readline())  # 버스 경로 개수
    edges = [list(map(int, readline().split())) for _ in range(M)]  # U, V, T
    S, E = map(int, readline().split())  # 집 근처 버스 정류장 번호, 병원 근처 버스 정류장 번호

    answer = dijkstra(N, edges, S, E)
    write(str(answer)+'\n')
