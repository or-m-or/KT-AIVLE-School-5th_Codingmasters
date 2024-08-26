import sys
import math

read = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, read().split())
answer = math.gcd(N, M)
write(str(answer))


'''
최대 공약수 출력 -> math.gcd
'''
''' 
유클리드 알고리즘을 사용한 GCD 구현

유클리드 알고리즘은 두 자연수 또는 정수의 최대공약수를 계산하는 데 사용되는 알고리즘입니다.
- 두수 a와 b(a>b)의 최대 공약수는 b와 a로 나눈 나머지 (a mod b)의 최대 공약수와 같다.
- 이 과정을 b가 0이 될 때까지 반복하면, 그때의 a가 최대공약수가 된다.
'''
# a > b 일때
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
