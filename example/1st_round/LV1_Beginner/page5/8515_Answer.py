import sys
from decimal import Decimal, getcontext

readline = sys.stdin.readline
write = sys.stdout.write

p, q = map(int, readline().split()) # p: 분자, q: 분모
places = int(readline())

# Decimal의 정밀도 설정
getcontext().prec = places + 5  # 약간의 여유를 두어 정확도를 높임

# 분자와 분모를 Decimal 객체로 변환 후 나눗셈
result = Decimal(p) / Decimal(q)

# 결과 출력 (문자열 포맷팅을 사용하여 소수점 이하 places 자리까지 출력)
print(f"{result:.{places}f}")