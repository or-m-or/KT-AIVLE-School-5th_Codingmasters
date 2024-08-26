'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def rps_winner(a, b):
    '''
    1 : 가위, 2 : 바위, 3 : 보
    0 : 무승부, 1: a 승리, 2: b 승리
    '''
    if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
        return 2
    elif a == b:
        return 0
    else:
        return 1


def mukchippa(bot1: list, bot2: list) -> int:
    idx1, idx2 = 0, 0
    turn = 0  # 0: 선공을 정하는 단계, 1: 첫 번째 묵찌빠봇이 선공, 2: 두 번째 묵찌빠봇이 선공
    game_history = set()

    while True:
        state = (idx1, idx2, turn)
        if state in game_history:
            return 0
        game_history.add(state)

        move1 = bot1[idx1]
        move2 = bot2[idx2]
        idx1 = (idx1 + 1) % len(bot1)
        idx2 = (idx2 + 1) % len(bot2)

        if turn == 0:  # 선공을 정하는 단계
            winner = rps_winner(move1, move2)
            if winner != 0:
                turn = winner
        else:
            if turn == 1:  # 첫 번째 묵찌빠봇이 선공
                if move1 == move2:  # 선공 승리
                    return 1
                else:
                    winner = rps_winner(move1, move2)
                    if winner == 2:  # 공수 교대
                        turn = 2
            else:  # 두 번째 묵찌빠봇이 선공
                if move1 == move2:  # 선공 승리
                    return 2
                else:
                    winner = rps_winner(move1, move2)
                    if winner == 1:  # 공수 교대
                        turn = 1


if __name__ == "__main__":
    N, M = map(int, readline().split())
    bot1 = list(map(int, readline().split()))
    bot2 = list(map(int, readline().split()))

    ans = mukchippa(bot1, bot2)
    write(f'{ans}\n')
