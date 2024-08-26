'''
Type : 
'''
import sys
import math

readline = sys.stdin.readline


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    x = (10 * C) / A
    x = math.ceil(x)

    print(x)
