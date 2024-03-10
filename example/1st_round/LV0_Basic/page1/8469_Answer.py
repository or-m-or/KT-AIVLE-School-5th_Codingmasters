
''' 제출 1 : Original code '''
# import sys

# data = sys.stdin.readline().split()
# result = data[0]
# for i in range(1, len(data)):
#     result = result + ' ' + data[i]
#     if data[i] == 'c':
#         break
# print(result)


''' 제출 2 : 입출력 방법 최적화 '''
# import sys

# data = sys.stdin.readline().split()
# if 'c' in data:
#     result = ' '.join(data[:data.index('c')+1])
# else:
#     result = ' '.join(data)

# sys.stdout.write(result + '\n')


''' 제출 3 : 중복 연산 제거 '''
# import sys

# data = sys.stdin.readline().split()
# result = []  # 결과를 저장할 리스트 초기화

# # 'c'를 찾거나 모든 데이터를 확인할 때까지 반복
# for word in data:
#     result.append(word)
#     if word == 'c':
#         break  # 'c'를 찾으면 반복 중단

# # 결과를 출력
# sys.stdout.write(' '.join(result) + '\n')


''' 제출 4 : Generator로 메모리 아끼기 '''
import sys

def process_input(data):
    for word in data:
        yield word
        if word == 'c':
            break

input_data = sys.stdin.readline().split()
output_data = process_input(input_data)
sys.stdout.write(' '.join(output_data) + '\n')