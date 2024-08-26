import sys

readline = sys.stdin.readline


def solution(n, k, visitors):
    # 초기 K일 동안의 방문자 수 합계
    current_sum = sum(visitors[:k])
    max_sum = current_sum
    start_index = 0

    # 슬라이딩 윈도우로 나머지 기간의 합계 계산
    for i in range(1, n - k + 1):
        current_sum = current_sum - visitors[i - 1] + visitors[i + k - 1]
        if current_sum > max_sum:
            max_sum = current_sum
            start_index = i

    # 1부터 시작하는 인덱스 반환
    return start_index + 1


if __name__ == "__main__":
    N, K = map(int, readline().split())
    visitors = list(map(int, readline().split()))
    print(solution(N, K, visitors))
