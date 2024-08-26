import sys

read = sys.stdin.readline
write = sys.stdout.write

''' 
A : 첫째 항
B : 두항의 차이
N : 몇 번째 항
'''
A, B, N = map(int, read().split())
write(str(A + B * (N-1)))