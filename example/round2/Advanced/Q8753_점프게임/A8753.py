def jump_game(N, jump_limits):
    MOD = 1_000_000_007
    dp = [0] * (N + 1)
    dp[1] = 1

    for i in range(1, N + 1):
        for j in range(1, jump_limits[i - 1] + 1):
            if i + j <= N:
                dp[i + j] = (dp[i + j] + dp[i]) % MOD

    return dp[N]

if __name__ == "__main__":
    N = int(input())
    jump = list(map(int, input().split()))
    print(jump_game(N, jump))



# def jump_game(N, jump_limits):
#     MOD = 1_000_000_007
#     dp = [0] * (N + 1)
#     dp[1] = 1

#     for i in range(1, N + 1):
#         if dp[i] == 0:
#             continue
#         for j in range(1, jump_limits[i - 1] + 1):
#             if i + j <= N:
#                 dp[i + j] = (dp[i + j] + dp[i]) % MOD

#     return dp[N]

# if __name__ == "__main__":
#     N = int(input())
#     jump = list(map(int, input().split()))
#     print(jump_game(N, jump))



import sys
 
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
cnt = [0] * n
cnt[0] = 1
for i in range(n - 1):
    end = i + li[i] + 1 if i + li[i] + 1 < n else n
    for j in range(i + 1, end):
        cnt[j] = (cnt[j] + cnt[i]) % 1000000007
print(cnt[-1])