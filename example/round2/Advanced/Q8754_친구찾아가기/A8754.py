from collections import deque

def solution(N, heights):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[[False, False] for _ in range(N)] for _ in range(N)]
    queue = deque([(0, 0, 0, 1)])  # (x, y, used_jump, path_length)
    visited[0][0][0] = True

    while queue:
        x, y, used_jump, length = queue.popleft()

        if x == N - 1 and y == N - 1:
            return length

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if heights[nx][ny] <= heights[x][y] and not visited[nx][ny][used_jump]:
                    visited[nx][ny][used_jump] = True
                    queue.append((nx, ny, used_jump, length + 1))
                elif heights[nx][ny] > heights[x][y] and used_jump == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, 1, length + 1))

    return -1


if __name__ == "__main__":
    N = int(input())
    heights = [ list(map(int, input().split())) for _ in range(N)]
    print(solution(N, heights))