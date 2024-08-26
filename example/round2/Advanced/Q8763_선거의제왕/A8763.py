import sys
from collections import deque


def calculate_min_moves(N, supporters):
    """
    최소 이동 횟수를 계산하는 함수
    """
    me = supporters[0]
    supporters = supporters[1:]
    supporters.sort(reverse=True)

    if me > supporters[0]:
        return 0
    elif me == supporters[0]:
        return 1
    else:
        total = me
        idx = len(supporters)
        for i in range(N - 1):
            total += supporters[i]
            if supporters[i] <= total // (i + 2):
                total -= supporters[i]
                supporters = supporters[:i]
                idx = i
                break
        answer = 0
        avg = (me + sum(supporters)) // (1 + len(supporters)) + 1
        for i in range(idx):
            gap = supporters[i] - avg
            answer += gap
            supporters[i] -= gap
            me += gap

        supporters = deque(supporters[:idx])
        comp = supporters.popleft()
        while me <= comp:
            me += 1
            comp -= 1
            answer += 1
            supporters.append(comp)
            comp = supporters.popleft()
        return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    supporters = list(map(int, sys.stdin.readline().strip().split()))
    result = calculate_min_moves(N, supporters)
    print(result)

