import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())

if N % 2 == 1:
    write('RUN')
else:
    write('STAY')