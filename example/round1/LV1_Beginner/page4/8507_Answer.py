import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())

for i in range(1,N):
    if i < 7 and N-i < 7:
        write(''.join(f'{i} {N-i}\n'))