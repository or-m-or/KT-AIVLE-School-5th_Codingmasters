'''
Type : 
'''
import sys

readline = sys.stdin.readline

if __name__ == "__main__":
    A, B, C = map(int, input().split())

    # 가장 많은 용액의 개수와 나머지 두 용액의 개수를 비교
    if max(A, B, C) > (A + B + C - max(A, B, C)):
        print("NO")
    else:
        print("YES")
