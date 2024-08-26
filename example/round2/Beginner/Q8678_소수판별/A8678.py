'''
Type : 소수판별법
'''
import sys
import math

readline = sys.stdin.readline
write = sys.stdout.write


def is_prime_number(number: int) -> int:
    if number < 2:
        return 0
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i == 0:
            return 0
    return 1


if __name__ == "__main__":
    A = int(readline())
    write(str(is_prime_number(A)))
