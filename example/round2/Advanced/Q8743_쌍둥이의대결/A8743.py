# def calculate_score(sequence, m):
#     n = len(sequence)
#     score = [[0] * n for _ in range(n)]

#     # 구간 [i, j]의 점수를 미리 계산
#     for i in range(n):
#         product = 1
#         for j in range(i, n):
#             product = (product * sequence[j]) % m
#             score[i][j] = product

#     # dp 테이블 초기화
#     dp = [[0] * n for _ in range(n)]

#     # 구간 길이가 1인 경우의 dp 값 초기화
#     for i in range(n):
#         dp[i][i] = score[i][i]

#     # 구간 길이가 2 이상인 경우의 dp 값 계산
#     for length in range(2, n + 1):
#         for i in range(n - length + 1):
#             j = i + length - 1
#             dp[i][j] = max(score[i][j] - dp[i + 1][j], score[i][j] - dp[i][j - 1])

#     return dp[0][n - 1]


# # 입력 처리
# N = int(input().strip())
# sequence = list(map(int, input().strip().split()))
# M = int(input().strip())

# # 결과 계산 및 출력
# result = calculate_score(sequence, M)
# print(result)



def solution(n, sequence, m):
    scores = []
    
    for i in range(n):
        num = sequence[i] % m  
        scores.append(num)  
        for j in range(i + 1, n):
            num = (num * sequence[j]) % m  
            scores.append(num)    
    scores.sort(reverse=True)  
    
    answer = sum(scores[0::2]) - sum(scores[1::2])
    return answer
    
if __name__ == "__main__":
    N = int(input().strip())
    sequence = list(map(int, input().strip().split()))
    M = int(input().strip())
    result = solution(N, sequence, M)
    print(result)