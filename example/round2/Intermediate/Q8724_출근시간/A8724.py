'''
Type : 다익스트라
'''
import heapq


def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances


N, M, K = map(int, input().split())

graph = {i: {} for i in range(1, N+1)}

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u][v] = w

# 철수의 집에서 학교까지의 최단 경로
distances_from_home = dijkstra(graph, 1)

# 학교에서 회사까지의 최단 경로
distances_from_school = dijkstra(graph, K)

# 두 경로의 시간 합산
total_time = distances_from_home[K] + distances_from_school[N]

print(total_time)
