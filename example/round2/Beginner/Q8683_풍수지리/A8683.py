'''
Type : 완전탐색, 브루토포스?
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def check_same_blessing(grid: list, start_row: int, start_col: int, end_row: int, end_col: int) -> bool:
    """지정된 영역 내 모든 칸이 같은 기운을 내뿜는지 확인합니다."""
    initial_blessing = grid[start_row][start_col]
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            if grid[row][col] != initial_blessing:
                return False
    return True


def find_max_blessing(grid: list, rows: int, cols: int) -> int:
    """최대 축복을 받을 수 있는 영역의 크기를 찾습니다."""
    max_blessing = 1
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    if check_same_blessing(grid, start_row, start_col, end_row, end_col):
                        area = (end_row - start_row + 1) * \
                            (end_col - start_col + 1)
                        max_blessing = max(max_blessing, area)
    return max_blessing


if __name__ == "__main__":
    rows, cols = map(int, readline().split())
    grid = [readline().rstrip() for _ in range(rows)]

    answer = find_max_blessing(grid, rows, cols)
    write(str(answer))
