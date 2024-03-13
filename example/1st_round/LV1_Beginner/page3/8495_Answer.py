
''' solution 1 : 예외케이스 1개 통과 X - 2의 거듭제곱 개수의 입력 처리 X'''
# import sys

# read = sys.stdin.readline
# write = sys.stdout.write

# N = int(read())
# K = list(map(int, read().split()))

# root_node_length = [2,4,8,16,32,64,128,256,512,1024,2048,4096]

# for length in root_node_length:
#     if len(K) < length:
#         K = K + [0] * (length-len(K))
#         break

# tree = [K]
# while 1<len(K):
#     parents_node = []
#     for i in range(0,len(K),2):
#         parents_node.append(K[i] + K[i+1])
#     tree = [parents_node] + tree
#     K = parents_node

# for nodes in tree:
#     for node in nodes:
#         write(str(node)+' ')
#     write('\n')    


''' soluton 2  '''
'''
- 조건에 맞는 2의 거듭제곱 수 찾는 코드
bit_length() : 정수의 이진 표현에서 필요한 비트의 수를 반환
예를 들어, N = 6 (110 in binary)의 경우, bit_length()는 3을 반환합니다.
이는 6을 표현하기 위해 최소 3비트가 필요함

- 리스트 앞에 원소 추가 -> + 연산 혹은 list.insert(0, 값)

- sum(이터레이터) -> 원소 합 반환
'''
import sys

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())
K = list(map(int, read().split()))

# 최소 필요한 노드의 수를 계산하여 입력 리스트를 해당 길이로 맞춤
# 주어진 숫자 N에 대해, N을 포함하여 그 이상의 숫자 중에서 
# 가장 작은 2의 거듭제곱 수를 찾는 방법
# N에서 1을 빼는 이유는 N이 이미 2의 거듭제곱일 경우, 같은 값을 반환하기 위함
node_counts = 2**((N-1).bit_length())
K += [0] * (node_counts - N)  # 입력 리스트를 2의 거듭제곱 길이로 맞춤

tree = [K]
while len(K) > 1:
    K = [sum(K[i:i+2]) for i in range(0, len(K), 2)]
    tree.insert(0, K)

for level in tree:
    write(' '.join(map(str, level)))
    write('\n')
