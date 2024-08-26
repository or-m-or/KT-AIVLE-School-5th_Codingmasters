def solution(nums):
    from collections import defaultdict

    n = len(nums)
    dp = defaultdict(int)
    dp[0] = 1  # XOR가 0인 공집합

    for num in nums:
        new_dp = dp.copy()
        for xor_sum in dp:
            new_xor_sum = xor_sum ^ num
            new_dp[new_xor_sum] += dp[xor_sum]
        dp = new_dp

    return dp[0] - 1  # 공집합 제외

if __name__ == '__main__':
    N = int(input().strip())
    nums = list(map(int, input().strip().split()))
    result = solution(nums)
    print(result)
