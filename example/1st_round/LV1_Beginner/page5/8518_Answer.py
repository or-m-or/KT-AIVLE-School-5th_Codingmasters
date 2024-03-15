import sys

readline = sys.stdin.readline
write = sys.stdout.write

sides = list(map(int, readline().split()))
sides.sort()

if sides[2]**2 == sides[1]**2 + sides[0]**2:
    write('YES')
else:
    write('NO')