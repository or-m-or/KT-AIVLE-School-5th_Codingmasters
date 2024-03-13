import sys

read = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, read().split()) # N: 정점수, M: 간선수
node_info = [list(map(int, read().split())) for _ in range(M)]

matrix = [[0] * N for _ in range(N)]
for i in range(M):
    x = node_info[i][0]-1
    y = node_info[i][1]-1
    matrix[x][y] = 1
    matrix[y][x] = 1

for i in range(N):
    for j in range(N):
        write(str(matrix[i][j])+' ')
    write('\n')    
    