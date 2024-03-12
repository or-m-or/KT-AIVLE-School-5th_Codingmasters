
''' solution 1 '''
# import sys

# read = sys.stdin.readline
# write = sys.stdout.write

# N, target_name = read().split()
# name_list = list(read().split())

# for idx, name in enumerate(name_list):
#     if name == target_name:
#         ans = idx + 1

# write(str(ans))

''' solution 2 '''
import sys

read = sys.stdin.readline
write = sys.stdout.write

N, target_name = read().strip().split()
name_list = read().strip().split() # 리스트 반환 함!

ans = name_list.index(target_name) + 1

write(str(ans))

""" 
1. list.index( '원소' ) -> 해당 원소의 인덱스 반환!
2. read().strip().split() 의 반환 값은 list 이다.

"""
