import sys

readline = sys.stdin.readline


def solution(case1, case2):
    case1_2 = case1 + case1
    if case2 in case1_2:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    case1 = readline().strip()
    case2 = readline().strip()

    print(solution(case1, case2))
