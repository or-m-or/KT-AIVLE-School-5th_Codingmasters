'''
다시 풀기
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write

a,b = map(int, readline().split())

def generate_fibo(n):
    """
    Generate a Fibonacci sequence up to the n-th term.
    
    :param n: The number of terms to generate.
    :return: A list containing the Fibonacci sequence up to n terms.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    fibonacci = [1, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci


def sum_fibo_fibo(a, b):
    """
    Correctly calculate the sum of the Fibonacci Fibonacci sequence from the a-th to the b-th term.
    
    :param a: The starting term index.
    :param b: The ending term index.
    :return: The sum of the terms from a to b in the Fibonacci Fibonacci sequence.
    """
    # 기본 피보나치 수열 생성
    n = 50
    fibonacci = generate_fibo(n)
    
    # 피보나치 피보나치 수열의 각 항을 카운팅하는 데 사용될 변수들
    fibo_fibo_sum = 0
    current_index = 1  # 현재 항의 인덱스

    # 각 피보나치 수의 값을 그 수만큼 반복하면서 합계 계산
    for fibo_num in fibonacci:
        for _ in range(fibo_num):
            if current_index >= a and current_index <= b:
                fibo_fibo_sum += fibo_num
            elif current_index > b:
                break  # b항을 초과하면 더 이상 계산할 필요가 없음
            current_index += 1
            
    return fibo_fibo_sum


write(f'{sum_fibo_fibo(a,b)}\n')