from collections import deque


def solution(start_board):
    moves = [(-1, 2), (1, 2), (-2, 1), (-2, -1), (2, -1), (2, 1), (-1, -2), (1, -2)]

    start = []
    goal = []

    for i in range(3):
        for j in range(3):
            if start_board[i][j] == '1':
                start.append((i, j, '1'))
                goal.append((i, j, '2'))
            elif start_board[i][j] == '2':
                start.append((i, j, '2'))
                goal.append((i, j, '1'))

    start = tuple(sorted(start, key=lambda x: (x[2], x[0], x[1])))
    goal = tuple(sorted(goal, key=lambda x: (x[2], x[0], x[1])))

    queue = deque([start])
    seen = set()
    seen.add(start)

    while queue:
        current = queue.popleft()

        if current == goal:
            return "possible"

        for i, (x, y, color) in enumerate(current):
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 3 and 0 <= ny < 3:
                    if not any(nx == cx and ny == cy for cx, cy, c in current):
                        new_pos = (nx, ny, color)
                        new_state = list(current)
                        new_state[i] = new_pos
                        new_state = tuple(sorted(new_state, key=lambda x: (x[2], x[0], x[1])))
                        if new_state not in seen:
                            seen.add(new_state)
                            queue.append(new_state)

    return "impossible"


if __name__ == "__main__":
    chess = [input() for _ in range(3)]
    print(solution(chess))
