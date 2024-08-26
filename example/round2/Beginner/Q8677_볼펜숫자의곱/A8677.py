import sys

readline = sys.stdin.readline
write = sys.stdout.write


def max_product(N: int, numbers: list) -> int:
    numbers = sorted(numbers, reverse=True)

    case1 = numbers[0] * numbers[1]
    case2 = case1 * numbers[2]
    case3 = numbers[-1] * numbers[-2]
    case4 = case3 * numbers[0]

    return max(case1, case2, case3, case4)


if __name__ == "__main__":
    N = int(readline())
    numbers = list(map(int, readline().split()))
    answer = max_product(N, numbers)
    write(str(answer)+'\n')
