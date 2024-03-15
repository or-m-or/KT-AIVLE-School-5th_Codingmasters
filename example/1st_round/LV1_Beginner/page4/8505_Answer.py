import sys

readline = sys.stdin.readline
write = sys.stdout.write

H, M = map(int, readline().split())

if 29 < M:
    M -= 30
else:
    M += 30
    if H == 0:
        H = 23
    else:
        H -= 1

write(''.join(str(H)+' '+str(M)))