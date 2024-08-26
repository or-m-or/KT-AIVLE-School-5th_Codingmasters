import sys


''' solution 1 '''
read = sys.stdin.readline
write = sys.stdout.write

N, A = map(int, read().split())
data = list(map(int, read().split()))

try:
    A_location = data.index(A) + 1
    write(f'{A_location}')    
except:
    write('-1')


