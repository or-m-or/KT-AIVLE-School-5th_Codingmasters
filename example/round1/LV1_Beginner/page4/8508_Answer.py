import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline()) # 지원자 수
scores = [list(map(int, readline().split())) for _ in range(N)]





def compare_score(score1:list, score2:list):
    # 각 사람의 과목별 점수 할당
    p1_sub1, p1_sub2 = score1
    p2_sub1, p2_sub2 = score2

    # 조건 1: 한 사람의 성적이 모두 더 클 경우
    if (p1_sub1 > p2_sub1 and p1_sub2 > p2_sub2):
        return 'applicant1'
    elif (p2_sub1 > p1_sub1 and p2_sub2 > p1_sub2):
        return 'applicant2'
    
    # 조건 2: 한 과목 성적은 동일하고 다른 한 과목의 성적이 다를 때
    elif (p1_sub1 == p2_sub1 and p1_sub2 != p2_sub2):
        return 'applicant1' if p1_sub2 > p2_sub2 else 'applicant2'
    elif (p1_sub2 == p2_sub2 and p1_sub1 != p2_sub1):
        return 'applicant1' if p1_sub1 > p2_sub1 else 'applicant2'
    
    # 조건 3: 우열을 가릴 수 없는 경우
    else:
        return 'fail'
    


def ranking_corrected_integrated(scores: list) -> tuple:
    n = len(scores)
    lose_applicant = [[] for _ in range(n)]  # 각 지원자가 이긴 다른 지원자들의 번호를 저장
    none_list = []  # 서로 우열을 가릴 수 없는 지원자들의 그룹

    # 모든 지원자간 비교
    for i in range(n):
        for j in range(i + 1, n):
            result = compare_score(scores[i], scores[j])
            if result == 'applicant1':
                lose_applicant[i].append(j)
            elif result == 'applicant2':
                lose_applicant[j].append(i)

    # 서로 우열을 가릴 수 없는 지원자 그룹 찾기
    for i in range(n):
        for j in range(i + 1, n):
            if i not in lose_applicant[j] and j not in lose_applicant[i]:  # i와 j가 서로 이기지 못했으면
                found = False
                for group in none_list:
                    if i in group or j in group:
                        group.update([i, j])
                        found = True
                        break
                if not found:
                    none_list.append(set([i, j]))

    # 우열이 높은 순서로 none_list 정렬
    none_list_sorted = sorted(none_list, key=lambda x: -len(x))
    none_list_sorted = [list(group) for group in none_list_sorted]  # set을 list로 변환

    # none_list를 기반으로 lose_applicant 정제
    for group in none_list_sorted:
        common_losers = set(lose_applicant[group[0]])  # 첫 번째 지원자가 이긴 지원자들을 기준으로 시작
        for i in group[1:]:
            common_losers.intersection_update(set(lose_applicant[i]))  # 공통 원소만 남김

        # 공통으로 이긴 지원자들로 lose_applicant 업데이트
        for i in group:
            lose_applicant[i] = list(common_losers)

    return lose_applicant, none_list_sorted



def ranking_corrected_integrated_final(scores: list) -> list:
    n = len(scores)
    _, none_list_sorted = ranking_corrected_integrated(scores)
    ranks = [None] * n  # 각 지원자의 등수를 저장할 리스트 초기화

    # none_list_sorted를 사용하여 등수 할당
    current_rank = 1
    for group in none_list_sorted:
        for i in group:
            ranks[i] = current_rank
        current_rank += len(group)

    # none_list_sorted에 속하지 않은 지원자들에게 등수 할당
    for i in range(n):
        if ranks[i] is None:
            ranks[i] = current_rank
            current_rank += 1

    return ranks

# # 수정된 함수 테스트
# scores_test_case = [[62, 53], [36, 53]]
# final_ranks_test_case = ranking_corrected_integrated_final(scores_test_case)
# print("Final Ranks for the test case:", final_ranks_test_case)













# print(ranking(scores))
# print(" ".join(map(str, ranks)))