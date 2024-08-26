'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def solution(N):
    if N == 1:
        return 0
    lines = 0
    max_regions = 1
    while max_regions < N:
        lines += 1
        max_regions = (lines * (lines + 1)) // 2 + 1
    return lines


if __name__ == "__main__":
    N = int(readline())
    write(f'{solution(N)}\n')
