import sys
from math import ceil


""" try 1 """
def solution(A, B, N):
    day = 1 # 반복횟수 세기
    count = 0 # 푼 문제수 (종료조건)
    
    while(True):
        count = count + A
        if count >= N:
            break
        count = count - B
        day += 1
    
    return str(day)


""" try 2 """
def cal_remember_day(remember: int, forget: int, task_num: int) -> str:
    if task_num <= remember:
        day = 1
    else:
        day = ceil((task_num - remember) / (remember - forget) + 1)
    return str(day)
    
    
if __name__ == "__main__":
    read = sys.stdin.readline
    write = sys.stdout.write
    
    A, B, N = map(int, read().split())
    day = cal_remember_day(remember=A, forget=B, task_num=N)        
    write(day)