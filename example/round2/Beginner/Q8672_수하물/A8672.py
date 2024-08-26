# 무게, 가격
# 가방 K개- 무게 제한 , 1개
# 물건 가방정보
# 물건들의 가격합 최대

# 물건개수 N 가방 수 K
# 물건 무게 M 가격  V - N개
# 무게제한 C - K개
'''
Type : 우선순위 큐
'''
import sys
import heapq

readline = sys.stdin.readline
write = sys.stdout.write


def max_value(N, K, items, bags):
    items.sort(key=lambda x: x[0])  # lambda 매개변수 : 반환식
    bags.sort()

    price_sum = 0
    temp = []  # 우선순위 큐

    for bag in bags:
        while items and bag >= items[0][0]:
            heapq.heappush(temp, -items[0][1])
            heapq.heappop(items)
        if temp:
            price_sum += -heapq.heappop(temp)
        elif not items:
            break

    return price_sum


if __name__ == "__main__":
    N, K = map(int, readline().split())
    items = [list(map(int, readline().split())) for _ in range(N)]
    bags = [int(readline()) for _ in range(K)]

    answer = max_value(N, K, items, bags)
    write(str(answer)+'\n')
