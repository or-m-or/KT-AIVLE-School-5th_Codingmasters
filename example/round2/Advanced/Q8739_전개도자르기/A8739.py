class CubeSumSolver:
    def __init__(self, grid):
        self.grid = grid
        self.base_patterns = self._gen_base_patterns()
        self.patterns = self._gen_trans_patterns(self.base_patterns)

    def _gen_base_patterns(self):
        """
        기본 전개도 패턴을 생성하는 함수
        """
        return [
            [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (0, -1)],
            [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, -1)],
            [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (2, -1)],
            [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (3, -1)],
            [(0, 0), (1, 0), (2, 0), (3, 0), (1, 1), (1, -1)],
            [(0, 0), (1, 0), (2, 0), (3, 0), (1, 1), (2, -1)],
            [(0, 0), (1, 0), (2, 0), (0, 1), (2, -1), (3, -1)],
            [(0, 0), (1, 0), (2, 0), (1, 1), (2, -1), (3, -1)],
            [(0, 0), (1, 0), (2, 0), (2, 1), (2, -1), (3, -1)],
            [(0, 0), (1, 0), (2, 0), (2, -1), (3, -1), (4, -1)],
            [(0, 0), (1, 0), (1, -1), (2, -1), (2, -2), (3, -2)]
        ]

    def _rot(self, p):
        """
        패턴을 90도 회전시키는 함수
        """
        return [(-y, x) for x, y in p]

    def _flip_h(self, p):
        """
        패턴을 수평으로 대칭시키는 함수
        """
        return [(-x, y) for x, y in p]

    def _flip_v(self, p):
        """
        패턴을 수직으로 대칭시키는 함수
        """
        return [(x, -y) for x, y in p]

    def _gen_trans_patterns(self, base_patterns):
        """
        기본 전개도 패턴을 다양한 변환(회전 및 대칭)하여 모든 패턴을 생성하는 함수
        """
        trans_patterns = set()
        for p in base_patterns:
            for _ in range(4):
                p = self._rot(p)
                trans_patterns.add(tuple(p))
                trans_patterns.add(tuple(self._flip_h(p)))
                trans_patterns.add(tuple(self._flip_v(p)))
        return [list(p) for p in trans_patterns]

    def max_cube_sum(self):
        """
        격자에서 가능한 모든 전개도를 적용하여 정육면체에 쓰인 수의 합의 최대값을 찾는 함수
        """
        n = len(self.grid)
        max_sum = 0
        for x in range(n):
            for y in range(n):
                for p in self.patterns:
                    current_sum = 0
                    valid = True
                    for dx, dy in p:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            current_sum += self.grid[nx][ny]
                        else:
                            valid = False
                            break
                    if valid:
                        max_sum = max(max_sum, current_sum)
        return max_sum

    @staticmethod
    def get_grid():
        """
        격자를 입력받는 함수
        """
        grid = []
        for _ in range(10):
            row = list(map(int, input().split()))
            grid.append(row)
        return grid


if __name__ == "__main__":
    grid = CubeSumSolver.get_grid()
    solver = CubeSumSolver(grid)
    result = solver.max_cube_sum()
    print(result)
