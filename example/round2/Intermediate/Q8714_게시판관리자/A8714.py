from itertools import combinations

def solution(n, s1, s2):
    # 서로 다른 단어의 인덱스 수집
    diff_indices = [i for i in range(n) if s1[i] != s2[i]]

    # 두 문장이 동일한 경우
    if not diff_indices:
        return 0

    # 서로 다른 단어들만 추출
    s1_diff = [s1[i] for i in diff_indices]
    s2_diff = [s2[i] for i in diff_indices]

    cands = set() # 가능한 단어의 조합
    # 첫 번째 문장의 가능한 단어 교환 조합 생성
    for i, j in combinations(range(len(s1_diff)), 2):
        s1_diff[i], s1_diff[j] = s1_diff[j], s1_diff[i]
        cands.add(tuple(s1_diff))
        s1_diff[i], s1_diff[j] = s1_diff[j], s1_diff[i] # 복원

    answer = 0
    # 두 번째 문장의 가능한 단어 교환 조합과 비교
    for i, j in combinations(range(len(s2_diff)), 2):
        s2_diff[i], s2_diff[j] = s2_diff[j], s2_diff[i]
        if tuple(s2_diff) in cands:
            answer += 1
        s2_diff[i], s2_diff[j] = s2_diff[j], s2_diff[i] # 복원

    return answer


if __name__ == "__main__":
    N = int(input())
    sentence1 = input().split()
    sentence2 = input().split()
    answer = solution(N, sentence1, sentence2)
    print(answer)

