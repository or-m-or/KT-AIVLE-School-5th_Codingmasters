class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal(N, edges):
    edges.sort(key=lambda x: x[2])  
    uf = UnionFind(N)
    total_cost = 0

    for u, v, cost in edges:
        if uf.union(u - 1, v - 1):  
            total_cost += cost

    return total_cost


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    for i in range(N - 1):
        edges.append([i + 1, i + 2, K])
    print(kruskal(N, edges))