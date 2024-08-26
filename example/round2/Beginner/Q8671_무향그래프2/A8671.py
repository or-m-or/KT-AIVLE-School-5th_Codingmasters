'''
Type : Greedy
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write

if __name__=="__main__":
    N, M = map(int, readline().split())
    graph = {i: set() for i in range(1, N+1)}
    
    for _ in range(M):
        v1, v2 = map(int, readline().split())
        graph[v1].add(v2)
        graph[v2].add(v1)
    
    for i in range(1, N+1):
        if graph[i]:
            write(' '.join(map(str, sorted(graph[i]))))
        else:
            write('no')
        write('\n')