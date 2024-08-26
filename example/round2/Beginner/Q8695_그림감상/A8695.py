'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def find_2x2_square(board):
    for i in range(3):  # 3행까지만 검사 (2x2 크기 때문에)
        for j in range(3):  # 3열까지만 검사
            # 현재 2x2 영역의 칸들
            cells = [
                board[i][j], board[i][j+1],
                board[i+1][j], board[i+1][j+1]
            ]
            # 'X' 개수 세기
            count_x = cells.count('X')

            # 4개 모두 X이면 이미 2x2 X 영역이 존재
            # 3개가 X이고 하나가 O라면 마법의 붓 사용으로 2x2 X 영역 가능
            if count_x == 4 or count_x == 3:
                return "yes"
    return "no"


if __name__ == "__main__":
    board = [list(input().strip()) for _ in range(4)]
    write(f'{find_2x2_square(board)}\n')
