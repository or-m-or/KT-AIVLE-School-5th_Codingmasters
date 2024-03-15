# 예제 입력
N, M = 4, 3
palace = [
    [0, 1, 1],
    [1, 0, 0],
    [0, 1, 0],
    [1, 0, 1]
]

# 각 가로줄과 세로줄에 대해 기둥(0)이 있는지 확인
rows_with_pillars = [any(row[m] == 0 for m in range(M)) for row in palace]
cols_with_pillars = [any(palace[n][m] == 0 for n in range(N)) for m in range(M)]

# 기둥이 없는 가로줄과 세로줄의 수 계산
missing_pillars_in_rows = sum(not has_pillar for has_pillar in rows_with_pillars)
missing_pillars_in_cols = sum(not has_pillar for has_pillar in cols_with_pillars)

# 세워야 하는 기둥의 최솟값 계산
min_pillars_to_add = max(missing_pillars_in_rows, missing_pillars_in_cols)

min_pillars_to_add
