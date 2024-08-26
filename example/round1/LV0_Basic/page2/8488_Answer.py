import sys
import math

def count_prime_number(N:int)->int:
    array = [False, False] + [True]*(N-1)
    count=0

    for i in range(2, N+1):
        if array[i]:
            count += 1
            for j in range(2*i, N+1, i):
                array[j] = False

    return count


if __name__=="__main__":
    read = sys.stdin.readline
    write = sys.stdout.write

    N = int(read())
    answer = count_prime_number(N)
    write(str(answer))




"""
소수 판별하기
"""
# 방법1 단점 : x의 값이 커지면 오래걸림
def is_prime_number1(x):
    ''' 소수 판별 기본적인 방법 '''
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
# print('1-1) 소수판별 방법 1 (input:4) : ',is_prime_number1(4)) # return False
# print('1-2) 소수판별 방법 1 (input:7) : ',is_prime_number1(7)) # return True


# 방법 1 문제 해결함
# 방법2 단점 : 특정한 숫자 X가 소수인지만 판별하므로, 
# 일정 범위 내의 모든 숫자에 대한 소수를 찾으려면 모든 숫자를 검증해야 하므로 오래걸림
import math
def is_prime_number2(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)+1)): # 2부터 x의 제곱근까지만 고려
        if x % i == 0:
            return False
    return True
# print('2) 소수판별 방법 2 (input:1042) : ',is_prime_number2(1042))


# 방법 3 : 방법2 문제 해결(에라토스테네스의 체), 특정 범위 내 여러개의 숫자들 중 소수인 숫자만 반환
# 1. 2부터 N까지 존재하는 모든 자연수 중에서 가장 작은 수를 x로 지정
# 2. 나열된 숫자 중 x의 배수 제거
# 3. 더 이상 제거되지 않을 때까지 1,2번 반복
import math

n = 1000 # 2부터 1000까지의 수 중 소수 찾음
array = [False, False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
    if array[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            array[j] = False
# print('3) 소수판별 방법 3 (input:1000), 0~1000 중 소수인 값 리스트 반환 : \n',primes, '\n')

