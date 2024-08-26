'''
Type : DFS
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def dfs(board, x, y, N, M):
    if x < 0 or x >= N or y < 0 or y >= M:
        return

    if board[x][y] == '0':
        board[x][y] = '1'
        dfs(board, x-1, y, N, M)
        dfs(board, x+1, y, N, M)
        dfs(board, x, y-1, N, M)
        dfs(board, x, y+1, N, M)
        return True
    return False


if __name__ == "__main__":
    N, M = map(int, readline().split())
    board = [list(readline()) for _ in range(N)]

    count = 0
    for i in range(N):
        for j in range(M):
            if dfs(board, i, j, N, M) == True:
                count += 1

    write(str(count)+'\n')
