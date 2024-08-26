from collections import defaultdict, deque
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def adjust_weights(graph, weights, K):
    # 각 정점에 대한 최소 비용을 저장할 배열 초기화
    min_cost = [0] * len(weights)

    # 모든 정점에 대해 반복
    for start_v in range(1, len(weights)):
        # 해당 정점에서 시작하는 BFS 실행
        queue = deque()
        queue.append(start_v)
        visited = [False] * len(weights)
        visited[start_v] = True

        while queue:
            cur_v = queue.popleft()

            for next_v in graph[cur_v]:
                if not visited[next_v]:
                    visited[next_v] = True
                    queue.append(next_v)
                    # 현재 정점과 다음 정점 간의 가중치 차이 계산
                    weight_diff = abs(weights[cur_v] - weights[next_v])
                    # 가중치 차이가 K 이하로 만들기 위해 필요한 비용 계산
                    if weight_diff > K:
                        additional_cost = weight_diff - K
                        # 다음 정점의 가중치를 현재 정점의 가중치 + K 또는 -K로 조정
                        if weights[cur_v] > weights[next_v]:
                            min_cost[next_v] += additional_cost
                            weights[next_v] += additional_cost
                        else:
                            min_cost[cur_v] += additional_cost
                            weights[cur_v] += additional_cost
    return sum(min_cost)


if __name__ == "__main__":
    N, M, K = map(int, readline().split())

    weights = [0]
    for i in range(N):
        weights.append(int(readline()))

    graph = defaultdict(list)
    for _ in range(M):
        vertax1, vertax2 = map(int, readline().split())
        graph[vertax1].append(vertax2)
        graph[vertax2].append(vertax1)

    total_cost = adjust_weights(graph, weights, K)
    write(f'{total_cost}\n')
