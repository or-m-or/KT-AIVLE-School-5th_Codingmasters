'''
Type : BFS
'''
from collections import defaultdict, deque
import sys
# from collections import deque

readline = sys.stdin.readline
write = sys.stdout.write


def bfs(graph, weights, start_v, K):
    queue = deque()
    queue.append(start_v)
    visited = [False] * len(weights)
    visited[start_v] = True
    cost = 0

    while queue:
        cur_v = queue.popleft()
        cur_weight = weights[cur_v]

        for next_v in graph[cur_v]:

            if visited[next_v] == False:
                new_weight = weights[next_v]

                if abs(cur_weight - new_weight) > K:

                    if cur_weight > new_weight:
                        target_weight = cur_weight - K
                        cost += target_weight - new_weight
                        weights[next_v] = target_weight

                    else:
                        target_weight = new_weight - K
                        cost += target_weight - cur_weight
                        weights[cur_v] = target_weight
                        visited[next_v] = False
                        visited[cur_v] = False
                        queue.append(next_v)
                        queue.append(cur_v)
                        continue

                visited[next_v] = True
                queue.append(next_v)

    return cost


if __name__ == "__main__":
    N, M, K = map(int, readline().split())

    weights = [0]
    for i in range(N):
        weights.append(int(readline()))

    graph = {}
    for _ in range(M):
        vertax1, vertax2 = map(int, readline().split())
        if vertax1 in graph:
            graph[vertax1].append(vertax2)
        else:
            graph[vertax1] = [vertax2]

        if vertax2 in graph:
            graph[vertax2].append(vertax1)
        else:
            graph[vertax2] = [vertax1]

    # print(weights)
    # print(graph)
    start_v = weights.index(max(weights))
    write(f'{bfs(graph, weights, start_v, K)}\n')

    # # test1
    # N, M, K = 3, 3, 5
    # weights = [0, 1, 10, 20]
    # graph = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    # start_v = weights.index(max(weights))
    # write(f'test1 : {bfs(graph, weights, start_v, K)} (19)\n')

    # # test2
    # N, M, K = 5, 4, 1
    # weights = [0, 10, 20, 30, 40, 50]
    # graph = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4]}
    # start_v = weights.index(max(weights))
    # write(f'test2 : {bfs(graph, weights, start_v, K)} (90)\n')

    # # test3
    # N, M, K = 7, 6, 5
    # weights = [0, 100, 90, 80, 70, 95, 98, 97]
    # graph = {1: [2, 3], 2: [1, 4, 5], 3: [
    #     1, 6, 7], 4: [2], 5: [2], 6: [3], 7: [3]}
    # start_v = weights.index(max(weights))
    # write(f'test3 : {bfs(graph, weights, start_v, K)} (40)\n')

    # # test 4
    # N, M, K = 7, 6, 5
    # weights = [0, 100, 90, 80, 70, 80, 90, 100]
    # graph = {1: [2], 2: [1, 3], 3: [2, 4], 4: [
    #     3, 5], 5: [4, 6], 6: [5, 7], 7: [6]}
    # start_v = weights.index(max(weights))
    # write(f'test4 : {bfs(graph, weights, start_v, K)} (45)\n')

    # # test 5
    # N, M, K = 7, 6, 5
    # weights = [0, 100, 90, 80, 90, 10, 90, 70, 90, 100]
    # graph = {1: [2, 4], 2: [1, 3, 5], 3: [2, 6], 4: [1, 7, 5], 5: [
    #     2, 8, 4, 6], 6: [3, 9, 5], 7: [4, 8], 8: [5, 7, 9], 9: [6, 8]}
    # start_v = weights.index(max(weights))
    # write(f'test5 : {bfs(graph, weights, start_v, K)} (130)\n')
