def find(parent, i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent, parent[i])
        return parent[i]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def solution(N, M, beauties, edges):
    weighted_edges = []
    for u, v in edges:
        weighted_edges.append((beauties[u - 1] + beauties[v - 1], u - 1, v - 1))
    
    weighted_edges.sort(reverse=True, key=lambda x: x[0])
    
    parent = [i for i in range(N)]
    rank = [0] * N
    
    max_beauty = 0
    edge_count = 0
    
    for weight, u, v in weighted_edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            max_beauty += weight
            edge_count += 1
            if edge_count == N - 1:
                break
    
    return max_beauty

if __name__=="__main__":
    N, M = map(int, input().split())
    beauties = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    print(solution(N, M, beauties, edges))
