'''
Type : 
'''


def solution(L, R):
    # 가능한 쌍의 개수 초기화
    count = 0

    # 가능한 모든 합 s에 대해서, s는 B+C로, A=s인 케이스
    for s in range(2 * L, 2 * R + 1):
        # A는 s와 같으며 L과 R 사이에 있어야 함
        if L <= s <= R:
            # B는 최소 L이고 최대 R
            # C도 최소 L이고 최대 R
            # B와 C의 조합이 만들 수 있는 최소값은 2L, 최대값은 2R
            # B를 L부터 시작하여 가능한 최대값은 min(R, s-L)
            # B와 C의 각 조합을 계산할 때, B와 C는 서로 독립적으로 선택 가능
            # B+C=s이므로, B가 정해지면 C=s-B
            min_B = L
            max_B = min(R, s - L)
            if min_B <= max_B:
                count += (max_B - min_B + 1)

    return count


if __name__ == "__main__":
    L, R = map(int, input().split())
    print(solution(L, R))
