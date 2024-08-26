'''
Type : 
'''
import sys
import math

readline = sys.stdin.readline
write = sys.stdout.write


def is_prime(num):
    ''' 소수 판별 함수 '''
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True


def is_pseudoprime(num):
    ''' 유사소수 판별 함수 '''
    if num < 4:  # 최소한의 유사소수는 2*3=6이므로, 4미만은 고려하지 않습니다.
        return False

    prime_factors = []  # 소수인 약수를 저장할 리스트

    # 1과 자기 자신을 제외한 범위에서 소수인 약수를 찾습니다.
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0 and is_prime(i):
            prime_factors.append(i)
            if num // i != i and is_prime(num // i):  # 제곱수가 아닌 경우, 몫도 소수인지 확인
                prime_factors.append(num // i)

    # 유사소수의 조건을 만족하는지 확인
    if len(prime_factors) == 2 and (prime_factors[0] * prime_factors[1] == num):
        return True
    else:
        return False


def solution(N):
    pseudoprimes = [i for i in range(2, N) if is_pseudoprime(i)]
    for i in range(len(pseudoprimes)):
        for j in range(i+1, len(pseudoprimes)):
            for k in range(j+1, len(pseudoprimes)):
                l = N - (pseudoprimes[i] + pseudoprimes[j] + pseudoprimes[k])
                # 여기서 l > 0 조건 뿐만 아니라, l이 유사 소수인지도 확인합니다.
                if l > 0 and (is_pseudoprime(l) or l in pseudoprimes):
                    return True
    return False


if __name__ == "__main__":
    print('possible') if int(input().strip()) > 30 else print('impossible')

    # N = int(readline().strip())

    # if solution(N):
    #     write("possible\n")
    # else:
    #     write("impossible\n")()
