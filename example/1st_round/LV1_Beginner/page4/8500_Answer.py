'''
북마크 - 알고리즘 참고
'''
import sys
from math import factorial


def combination(A, B):
    return factorial(A) // (factorial(B) * factorial(A - B))


read = sys.stdin.readline
write = sys.stdout.write

n, r = map(int, read().split())
write(str(combination(n, r)))
