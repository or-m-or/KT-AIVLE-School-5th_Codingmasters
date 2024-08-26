'''
Type : DFS
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write

def dfs(cur_v:int, graph:dict, visited:dict):
    visited.append(cur_v)
    write(f'{str(cur_v)} ')
    
    for next_v in sorted(graph[cur_v]):
        if next_v not in visited:
            dfs(next_v, graph, visited)

            
if __name__=="__main__":
    N, M = map(int, readline().split())
    graph = {i: set() for i in range(1, N+1)}
    visited = []
    
    for _ in range(M):
        A, B = map(int, readline().split())
        graph[A].add(B)
        graph[B].add(A)

    dfs(1, graph=graph, visited=visited)
    write('\n')