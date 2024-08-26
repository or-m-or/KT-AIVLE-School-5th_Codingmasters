'''
Type : 
'''

if __name__ == "__main__":
    N, K = map(int, input().split())
    performances = list(map(int, input().split()))

    # 배우별 마지막으로 연기하는 날짜를 저장하는 딕셔너리
    last_seen = {}

    # 처음에는 모든 배우를 아직 보지 못했으므로, 각 배우의 마지막 연기 날짜를 -1로 초기화
    for i in range(1, K+1):
        last_seen[i] = -1

    min_days = N  # 최소 일수를 최대로 설정하여 초기화
    window_start = 0

    for window_end in range(N):
        # 현재 배우의 마지막 연기 날짜를 업데이트
        last_seen[performances[window_end]] = window_end

        # 만약 모든 배우가 이 구간에서 최소 한 번 이상 연기했다면,
        # 현재 구간의 크기(일수)를 계산하고, 이전에 계산한 최소 일수와 비교하여 업데이트
        if min(last_seen.values()) != -1:
            current_min_days = window_end - min(last_seen.values()) + 1
            min_days = min(min_days, current_min_days)

    # 최소 일수 출력
    print(min_days)
