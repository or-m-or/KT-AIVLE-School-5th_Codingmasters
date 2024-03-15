'''
DP(Dynamic Programming, 동적계획법)
다시 풀기 

- 다이나믹 프로그래밍
- 메모제이션
정리

'''
import sys

read = sys.stdin.readline
write = sys.stdout.write

# 정수 N을 입력받기
N = int(read())

# dp 테이블 초기화
dp = [0] * (N + 1)

# 초기 조건 설정
dp[1] = 1
dp[2] = 2

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
# 올바른 점화식을 이용한 dp 테이블 채우기
for i in range(3, N + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 796796


write(str(dp[N]))
