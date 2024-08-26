'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def solution(graph, N):
    visited = [False] * (N + 1)  # 구역의 번호가 1부터 시작하므로 N+1 크기로 초기화

    def dfs(cur_v):
        visited[cur_v] = True
        for next_v in graph.get(cur_v, []):
            if next_v == 1:  # 1번 구역으로 돌아올 수 있는 경우
                return True
            if not visited[next_v]:
                if dfs(next_v):
                    return True
        return False
    return dfs(1)


if __name__ == "__main__":
    N, M = map(int, input().split())  # N: 구역개수, M: 도로개수

    roadinfo = {}
    for _ in range(M):
        start_node, end_node = map(int, input().split())
        if start_node in roadinfo:
            roadinfo[start_node].append(end_node)
        else:
            roadinfo[start_node] = [end_node]

    # 1번 구역에서 시작하여 다른 구역을 거쳐 1번 구역으로 돌아올 수 있는지 확인
    if solution(roadinfo, N):
        write("YES\n")
    else:
        write("NO\n")
