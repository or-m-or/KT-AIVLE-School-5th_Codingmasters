import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())

cloudstar = '**'
for i in range(1,N):
    cloudstar = cloudstar + '\n' + ' '*i + '**'

write(cloudstar)