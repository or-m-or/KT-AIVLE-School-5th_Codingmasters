# import sys

# data = sys.stdin.readline().split()
# result = data[0]
# for i in range(1, len(data)):
#     result = result + ' ' + data[i]
#     if data[i] == 'c':
#         break
# print(result)

import sys

data = sys.stdin.readline().split()
if 'c' in data:
    result = ' '.join(data[:data.index('c')+1])
else:
    result = ' '.join(data)

print(result)