import sys

readline = sys.stdin.readline
write = sys.stdout.write

if __name__ == "__main__":
    A, B = map(int, readline().split())  # 기본 금액, 신용도
    N, M = map(int, readline().split())  # 옵션 개수, 선택할 옵션 개수
    option_price = [int(readline()) for _ in range(N)]

    option_price = sorted(option_price, reverse=True)
    option_price_sum = 0
    for i in range(M):
        option_price_sum += option_price[i]

    answer = A + B * option_price_sum
    write(str(answer)+'\n')
