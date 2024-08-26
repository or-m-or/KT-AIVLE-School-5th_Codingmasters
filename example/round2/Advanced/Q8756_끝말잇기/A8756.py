'''
Type : 미니맥스 알고리즘
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def can_win(words_by_start, used, last_char, turn):
    """
    이 함수는 현재 게임 상태에서 현재 턴의 플레이어가 승리할 수 있는지 판단합니다.
    `words_by_start`: 각 알파벳으로 시작하는 단어들을 리스트로 가지고 있는 딕셔너리
    `used`: 현재까지 사용된 단어들의 집합
    `last_char`: 직전에 사용된 단어의 마지막 문자
    `turn`: 현재 턴을 나타내는 변수, 0 또는 1 (0: 가영, 1: 나영)
    반환값은 현재 플레이어가 이길 수 있는 경우 True, 그렇지 않으면 False입니다.
    """
    if last_char in words_by_start:
        for word in words_by_start[last_char]:
            if word not in used:
                # 현재 플레이어가 선택할 수 있는 유효한 단어를 사용하고 게임 상태를 업데이트
                used.add(word)
                # 다음 턴 (상대방 턴)
                # 상대 플레이어의 턴에 이동하며, 상대가 패배하는 상황을 만들 수 있는지 확인
                if not can_win(words_by_start, used, word[-1], 1-turn):
                    used.remove(word)
                    return True
                # 사용했던 단어를 되돌림 (백트래킹)
                used.remove(word)

    # 모든 단어를 시도했지만 승리할 수 있는 방법이 없는 경우
    return False


def solve_game(words):
    """
    게임을 해결하는 메인 함수로, 각 단어의 시작 글자에 따라 단어를 분류하고, 게임의 승자를 결정합니다.
    `words`: 게임에 사용될 단어 리스트
    반환값은 가영이가 이길 수 있으면 "gayeong", 나영이가 이길 수 있으면 "nayeong"입니다.
    """
    # 시작 글자에 따라 단어를 분류
    words_by_start = {}
    for word in words:
        start = word[0]
        if start not in words_by_start:
            words_by_start[start] = []
        words_by_start[start].append(word)

    # 가영이가 먼저 시작하므로 초기 턴에서 모든 단어를 시작 단어로 시도
    for word in words:
        used = set([word])
        # 현재 단어로 시작했을 때 상대방이 패배하는 상황을 만들 수 있는지 확인
        if not can_win(words_by_start, used, word[-1], 1):
            return "gayeong"  # 가영이가 이길 수 있는 단어를 찾음

    return "nayeong"  # 모든 경우를 시도했으나 항상 나영이가 이김


if __name__ == "__main__":
    N = int(readline())
    words = [readline().strip() for _ in range(N)]

    write(f'{solve_game(words)}\n')

    # if N % 2 == 0:
    #     write('nayeong\n')
    # else:
    #     write('gayeong\n')
