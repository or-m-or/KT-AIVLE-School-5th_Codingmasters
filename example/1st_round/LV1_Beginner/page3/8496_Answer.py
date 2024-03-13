import sys

read = sys.stdin.readline
write = sys.stdout.write

K = list(map(int, read().split()))
K.sort()
write(str(K[2]))