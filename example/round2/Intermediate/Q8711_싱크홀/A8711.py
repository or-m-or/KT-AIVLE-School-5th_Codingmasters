'''
Type : Greedy
'''
import sys

readline = sys.stdin.readline


def minimum_planks(n, k, positions):
    positions.sort()
    count = 0
    i = 0

    while i < n:
        count += 1
        cover_end = positions[i] + k - 1
        while i < n and positions[i] <= cover_end:
            i += 1

    return count


if __name__ == "__main__":
    n, k = map(int, readline().split())
    positions = list(map(int, readline().split()))

    print(minimum_planks(n, k, positions))
