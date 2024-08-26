import sys

def remove_zero(number):
    if number.is_integer():
        return str(int(number))
    else:
        return str(number)


if __name__=="__main__":
    read = sys.stdin.readline
    write = sys.stdout.write

    PI = 3.14
    R = int(read().strip())
    
    area = remove_zero(R*R*PI)
    write(area)


"""
float -> int 변환 시 소수점 처리

방법 1. 명시적 타입 검사와 변환
- 더 빠른 방법
"""

def convert_if_integer(value):
    if value.is_integer():
        return int(value)
    else:
        return value

# # 예시
# value = 4.0
# converted_value = convert_if_integer(value)
# print(converted_value)  # 4, 정수형 출력

# value = 4.5
# converted_value = convert_if_integer(value)
# print(converted_value)  # 4.5, 실수형 그대로 유지

"""
방법 2. math.modf() 함수 사용
"""
import math

def convert_if_integer(value):
    fractional_part, integer_part = math.modf(value)
    if fractional_part == 0:
        return int(integer_part)
    else:
        return value

# # 예시
# value = 3.0
# converted_value = convert_if_integer(value)
# print(converted_value)  # 3, 정수형 출력

# value = 3.5
# converted_value = convert_if_integer(value)
# print(converted_value)  # 3.5, 실수형 그대로 유지