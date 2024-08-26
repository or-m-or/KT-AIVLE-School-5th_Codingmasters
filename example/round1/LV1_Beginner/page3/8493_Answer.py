'''
구현(정렬 구현)
'''

''' solution 1 - 제출 '''
# import sys

# read = sys.stdin.readline
# write = sys.stdout.write

# N = int(read())
# terms = [read().strip() for _ in range(N)]

# terms_dict = []
# for term in terms:
#     term_info = [len(term), term]
#     if term_info in terms_dict:
#         continue
    
#     terms_dict.append(term_info)
    
# terms_dict.sort()
# for i in range(len(terms_dict)):
#     write(terms_dict[i][1] + '\n')


''' solution 2'''
import sys

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())
terms = set(read().strip() for _ in range(N))

# 길이와 사전 순으로 정렬
sorted_terms = sorted(terms, key=lambda x: (len(x), x))

for term in sorted_terms:
    write(term + '\n')


'''
lambda 사용법

lambda arguments: expression
# arguments - 입력 인자
# expression - 반환 식

'''
