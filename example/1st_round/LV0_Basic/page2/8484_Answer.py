import sys

read = sys.stdin.readline
write = sys.stdout.write

N = int(read().strip())
write(str(N % 3))