'''
다시 보기

+ ''.join(map(str, non_zero_nums)) + '0'*zero
'''

''' solution 1 '''
# import sys

# readline = sys.stdin.readline
# write = sys.stdout.write

# N = int(readline())
# nums = list(map(int, readline().split()))

# zero = 0
# none_zero_nums = []
# for num in nums:
#     if num == 0:
#         zero += 1
#     else:
#         none_zero_nums.append(num)

# if zero < 2 or sum(none_zero_nums) % 3 != 0:
#     write('-1')
# else:
#     none_zero_nums.sort(reverse=True)
#     for num in none_zero_nums:
#         write(str(num))
#     write('0'*zero)


''' solution 2 '''
import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
nums = list(map(int, readline().split()))

zero = nums.count(0) # 0 개수
non_zero_nums = [num for num in nums if num != 0] # 0 제외 숫자 담은 리스트

if zero == 1 and len(non_zero_nums) < 1:
    write('0')
elif zero < 2 or sum(non_zero_nums) % 3 != 0:
    write('-1')
else:
    non_zero_nums.sort(reverse=True)
    write(''.join(map(str, non_zero_nums)) + '0'*zero)