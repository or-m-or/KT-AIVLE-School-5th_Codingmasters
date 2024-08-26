''' solution 1 '''
'''
단순 반복.
크기가 크면 실행 시간이 길어짐.
'''

import sys

read = sys.stdin.readline
write = sys.stdout.write

N, K = map(int, read().split()) # N: 민수좌표, K: 진희좌표

X = 0
moved_stair_count = 0
while moved_stair_count < K:
    X += 1
    moved_stair_count = N + 3*X

moved_stair_count + 3
moved_count = X + (moved_stair_count - K)

write(str(moved_count))


