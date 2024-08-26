from collections import deque


def bfs(maze, N, M):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([((0, 0), 0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while queue:
        (x, y), time = queue.popleft()

        if (x, y) == (N - 1, M - 1):
            return time

        for dx, dy in directions:
            # 두 칸 이동을 우선 시도
            nnx, nny = x + 2 * dx, y + 2 * dy
            if 0 <= nnx < N and 0 <= nny < M and maze[nnx][nny] == '.':
                if not visited[nnx][nny] and maze[x + dx][y + dy] == '.':  # 중간 칸도 체크
                    visited[nnx][nny] = True
                    queue.append(((nnx, nny), time + 1))
            else:
                # 두 칸 이동이 불가능하면 한 칸 이동 시도
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append(((nx, ny), time + 1))

    return -1


if __name__ == '__main__':
    N, M = map(int, input().split())
    maze = [input().strip() for _ in range(N)]
    result = bfs(maze, N, M)
    print(result)