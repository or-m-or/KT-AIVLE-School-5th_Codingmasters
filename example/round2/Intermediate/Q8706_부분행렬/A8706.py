'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def generate_subsets(arr):
    ''' 행렬의 모든 부분집합을 생성하는 함수 '''
    subsets = [[]]
    for num in arr:
        subsets += [curr + [num] for curr in subsets]
    return subsets


def calculate_sum(matrix, subset_rows, subset_cols):
    ''' 주어진 부분 행렬의 성분 합을 계산하는 함수 '''
    sum = 0
    for r in subset_rows:
        for c in subset_cols:
            sum += matrix[r][c]
    return sum


def check_submatrix_sum(matrix, N, M, X):
    # 행과 열의 인덱스 리스트 생성
    rows = [i for i in range(N)]
    cols = [i for i in range(M)]

    # 행과 열의 모든 가능한 부분집합 생성
    row_subsets = generate_subsets(rows)
    col_subsets = generate_subsets(cols)

    # 각 행과 열의 부분집합에 대해 성분의 합이 X와 같은 지 확인
    for subset_rows in row_subsets:
        for subset_cols in col_subsets:
            if calculate_sum(matrix, subset_rows, subset_cols) == X:
                return "YES"
    return "NO"


if __name__ == "__main__":
    N, M, X = map(int, readline().split())
    matrix = [list(map(int, readline().split())) for _ in range(N)]

    answer = check_submatrix_sum(matrix, N, M, X)
    write(f'{answer}\n')
