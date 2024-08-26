'''
Type : 
'''
import sys
from collections import Counter

readline = sys.stdin.readline
write = sys.stdout.write


def check_numbers(original, collected):
    # 숫자를 문자열로 변환 후 각 숫자의 빈도를 세기 위한 딕셔너리 생성
    original_count = {}
    collected_count = {}
    
    # 원래 숫자의 각 자릿수 세기
    for char in str(original):
        if char in original_count:
            original_count[char] += 1
        else:
            original_count[char] = 1

    # 주워담은 숫자의 각 자릿수 세기
    for char in str(collected):
        if char in collected_count:
            collected_count[char] += 1
        else:
            collected_count[char] = 1
    
    # 두 딕셔너리 비교
    if original_count == collected_count:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    num1 = int(readline())
    num2 = int(readline())

    answer = check_numbers(num1, num2)
    write(answer)
