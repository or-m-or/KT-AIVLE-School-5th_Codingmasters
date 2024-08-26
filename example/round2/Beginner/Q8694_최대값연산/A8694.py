'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def is_possible(x, y, z):
    # 가장 큰 값 z는 max(c, a)에 해당하므로, a 또는 c 중 하나는 z이어야 함
    # 두 번째로 큰 값 y는 max(b, c)에 해당하므로, b 또는 c 중 하나는 y이어야 함
    # 세 번째 값 x는 max(a, b)에 해당하므로, a 또는 b 중 하나는 x이어야 함

    # 가능한 a, b, c의 조합을 살펴보면:
    # a = x, b = y, c = z 또는 a = z, b = y, c = x (순서만 바뀐 케이스)
    # 주어진 x, y, z로 가능한지 체크

    # z는 최대값이어야 하며, c 또는 a이다.
    # 이 경우 c = z를 가정하고, b = y, a = x인 경우와
    # a = z를 가정하고, c = x, b = y인 경우를 검증할 수 있다.

    # 케이스 1: c = z, b = y, a = x
    if max(x, y) == z and max(y, z) == z and max(z, x) == z:
        return "possible"

    # 케이스 2: a = z, c = x, b = y
    if max(x, y) == z and max(y, x) == z and max(x, z) == z:
        return "possible"

    return "impossible"


if __name__ == "__main__":
    x, y, z = map(int, readline().split())
    write(f'{is_possible(x, y, z)}\n')
