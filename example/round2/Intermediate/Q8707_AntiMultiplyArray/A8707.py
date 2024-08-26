'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def solution(nums):
    # 두 수의 곱의 결과를 키로, 해당 곱을 만든 인덱스 쌍을 값으로 하는 해시맵 생성
    product_map = {}
    # YES 또는 NO를 출력할 변수
    answer = "NO"

    for i in range(len(nums)):
        for j in range(i+1, N):  # 중복을 피하기 위해 i+1부터 시작
            product = nums[i] * nums[j]  # 두 수의 곱 계산

            # 해당 곱을 이전에 계산한 적이 있는지 확인
            if product in product_map:
                # 같은 곱을 만든 적이 있고, 그 때의 인덱스 쌍과 현재의 인덱스 쌍이 모두 다르다면 YES
                for (prev_i, prev_j) in product_map[product]:
                    if prev_i != i and prev_i != j and prev_j != i and prev_j != j:
                        answer = "YES"
                        break
                if answer == "YES":
                    break
                # 같은 곱을 만든 적은 있지만, 모든 인덱스가 다르지 않은 경우 현재 인덱스 쌍 추가
                product_map[product].append((i, j))
            else:
                # 해당 곱을 처음 계산하는 경우, 인덱스 쌍 저장
                product_map[product] = [(i, j)]

        if answer == "YES":
            break

    return answer


if __name__ == "__main__":
    N = int(readline())
    A = list(map(int, readline().split()))

    write(f'{solution(A)}\n')
