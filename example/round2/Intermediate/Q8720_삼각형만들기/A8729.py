# def solution(N, nums):
#     nums.sort()

#     large_idx = N - 1
#     double_break = False
#     answer = 3
#     while large_idx > 2:

#         small_idx = 0
#         large = nums[large_idx]
#         while small_idx < large_idx -2:
#             if nums[small_idx] + nums[small_idx+1] <= large:
#                 small_idx += 1
#             else:
#                 answer = len(nums[small_idx:large_idx+1])
#                 double_break = True
#                 break

#         if double_break:
#             break
#         large_idx -= 1
#     return answer


# N = int(input())
# lengths = list(map(int, input().split()))
# print(solution(N, lengths))

# 케이스 1	Passed	1.538 s	
# 케이스 2	Passed	1.926 s	
# 케이스 3	Failed	1.347 s	
# 케이스 4	Passed	1.61 s	
# 케이스 5	Passed	1.674 s	
# 케이스 6	Passed	1.351 s	
# 케이스 7	Passed	1.336 s	



def solution(nums):
    nums.sort()  
    N = len(nums)
    
    for i in range(N, 2, -1):  
        for j in range(N - i + 1):  
            if nums[j] + nums[j + 1] > nums[j + i - 1]:
                return i 
    return 3  

if __name__ == "__main__":
    N = int(input()) 
    lengths = list(map(int, input().split())) 
    result = solution(lengths)  
    print(result)  