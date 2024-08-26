def max_sweetness(N, chocolates):
    dp = [[0] * (2 * N) for _ in range(2 * N)]
    extended_chocolates = chocolates + chocolates

    for i in range(2 * N):
        dp[i][i] = extended_chocolates[i][0]

    for length in range(2, N + 1):
        for i in range(2 * N - length + 1):
            j = i + length - 1
            dp[i][j] = max(dp[i][j - 1] + extended_chocolates[j][0] + (length - 1) * extended_chocolates[j][1],
                           dp[i + 1][j] + extended_chocolates[i][0] + (length - 1) * extended_chocolates[i][1])

    max_sweet = float('-inf')
    for i in range(N):
        max_sweet = max(max_sweet, dp[i][i + N - 1])

    return max_sweet


if __name__ == "__main__":
    N = int(input().strip())
    chocolates = [tuple(map(int, input().strip().split())) for _ in range(N)]
    result = max_sweetness(N, chocolates)
    print(result)
