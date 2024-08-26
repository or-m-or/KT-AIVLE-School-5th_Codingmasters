from itertools import product
import sys

# 비 효율적임

readline = sys.stdin.readline


def solution(N, M):
    count = 0
    colors = [1, 2, 3]  # Three different colors

    # Check if the current coloring is valid
    def is_valid(r, c, color, grid):
        if r > 0 and grid[r-1][c] == color:  # check top
            return False
        if c > 0 and grid[r][c-1] == color:  # check left
            return False
        return True

    # Recursive function to try coloring each cell
    def try_color(r, c, grid):
        nonlocal count
        if r == N:  # If we have colored all rows
            count += 1
            return

        next_r, next_c = (r, c + 1) if c + 1 < M else (r + 1, 0)

        for color in colors:
            if is_valid(r, c, color, grid):
                grid[r][c] = color
                try_color(next_r, next_c, grid)
                grid[r][c] = 0  # Reset color (backtrack)

    # Initialize an empty grid
    grid = [[0]*M for _ in range(N)]
    try_color(0, 0, grid)  # Start coloring from the top-left cell
    return count


if __name__ == "__main__":
    N, M = map(int, readline().split())
    answer = solution(N, M)
    print(answer)
