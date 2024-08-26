'''
Type : 
'''
import sys

readline = sys.stdin.readline


if __name__ == "__main__":
    N = int(readline())  # 축제 기간
    profits = list(map(int, readline().split()))  # 철수가 예측한 이익

    # 카데인 알고리즘을 사용하여 최대 이익 계산
    max_profit = cur_profit = profits[0]
    for i in range(1, N):
        cur_profit = max(profits[i], cur_profit + profits[i])
        max_profit = max(max_profit, cur_profit)

    # 만약 모든 예측 이익이 음수라면 최대 이익은 가장 작은 손실을 의미함
    print(max_profit if max_profit > 0 else max(profits))
