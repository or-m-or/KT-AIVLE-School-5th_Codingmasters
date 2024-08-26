'''
Type : 구현(진법 변환)
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def convert_length(num: int, base: int) -> int:
    length = 0
    while num > 0:
        num //= base
        length += 1
    return max(length, 1)


def find_min_base(file: list, M: int) -> int:
    for base in range(10, 63):
        temp_length = 0
        for num in file:
            temp_length += convert_length(num, base)
        temp_length += (len(file)-1)

        if temp_length <= M:
            return base
    return -1


if __name__ == "__main__":
    N, M = map(int, readline().split())
    file = list(map(int, readline().split()))

    min_base = find_min_base(file, M)
    write(str(min_base)+'\n')
