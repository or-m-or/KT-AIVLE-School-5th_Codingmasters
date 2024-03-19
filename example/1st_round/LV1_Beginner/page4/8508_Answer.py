import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline()) # 지원자 수
scores = [list(map(int, readline().split())) for _ in range(N)]



def select_winner(applicant1_score:list, applicant2_score:list) -> int:
    ''' 지원자 2명 중 이긴 사람의 번호(입력 받은 순서)를 반환, 비겼을 시에 0 반환 '''
    if applicant1_score[0] >= applicant2_score[0] and applicant1_score[1] >= applicant2_score[1]:
        if applicant1_score[0] == applicant2_score[0] and applicant1_score[1] == applicant2_score[1]:
            return 0 # 비김
        return 1 # 지원자 1 승리
    else:
        return 2 # 지원자 2 승리


def ranking(scores:list) -> list:
    ''' 지원자들의 점수를 입력 받고 등수를 반환 '''
    n = len(scores)
    ranks = [1] * n

    for i in range(n):
        for j in range(i + 1, n):
            winner = select_winner(scores[i], scores[j])
            
            if winner == 1:  # i가 j보다 우수한 경우
                ranks[j] = max(ranks[j], ranks[i] + 1)
            
            elif winner == 2:  # j가 i보다 우수한 경우
                ranks[i] = max(ranks[i], ranks[j] + 1)
            # winner == 0인 경우, 즉 우열을 가릴 수 없는 경우는 등수를 변경하지 않습니다.
            


# print(" ".join(map(str, ranks)))