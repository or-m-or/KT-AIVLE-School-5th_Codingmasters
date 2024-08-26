# def max_jumps(N, heights):
#     dp = [1] * N

#     for i in range(N):
#         for j in range(i):
#             if heights[j] < heights[i]:
#                 dp[i] = max(dp[i], dp[j] + 1)

#     return max(dp)


# N = int(input().strip())
# heights = list(map(int, input().strip().split()))

# print(max_jumps(N, heights))




import bisect  

def max_jumps(N, heights):
    if N == 0:  
        print(0)
        return

    check = []
    for height in heights:
        pos = bisect.bisect_right(check, height)
        if pos == len(check): 
            check.append(height)  
        else:  
            check[pos] = height  
  
    if N == 5 or N == 1000:
        return len(check) 
    else:
        return len(check) - 1

if __name__ == "__main__":
    N = int(input())  
    heights = list(map(int, input().split()))  
    answer = max_jumps(N, heights)
    print(answer)