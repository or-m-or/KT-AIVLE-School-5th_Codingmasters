'''
다시 보기

- 문자열은 리스트처럼 계산 가능!
'''

import sys

read = sys.stdin.readline 
write = sys.stdout.write

N = int(read())

count = [0]*10

for num in range(1, N+1):
    for digit in str(num):
        count[int(digit)] += 1

for i in count:
    write(str(i)+' ')