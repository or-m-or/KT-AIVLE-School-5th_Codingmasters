'''
Type : 
'''


def solution(N, K):
    # N까지의 홀수 개수
    count_odds = (N + 1) // 2

    if K <= count_odds:
        # K번째 홀수
        return 2 * K - 1
    else:
        # K번째 짝수
        count_evens = N // 2
        return 2 * (K - count_odds)


if __name__ == "__main__":
    N, K = map(int, input().split())
    print(solution(N, K))
