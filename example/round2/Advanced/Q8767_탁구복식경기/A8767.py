import itertools


def solution(N, skills):
    # 가능한 모든 4명의 조합을 구함
    min_diff = float('inf')
    for four_players in itertools.combinations(skills, 4):
        # 4명을 두 팀으로 나누기 위한 모든 2명씩의 조합 구하기
        pairs = list(itertools.combinations(four_players, 2))
        for i in range(len(pairs) // 2):
            team1 = pairs[i]
            team2 = pairs[len(pairs) - 1 - i]
            # 각 팀의 실력 계산
            skill1 = team1[0] * team1[1]
            skill2 = team2[0] * team2[1]
            # 지루한 정도 계산
            diff = abs(skill1 - skill2)
            # 최솟값 갱신
            min_diff = min(min_diff, diff)

    return min_diff


if __name__ == '__main__':
    N = int(input())
    skills = list(map(int, input().split()))
    print(solution(N, skills))


'''
예제 입력 2
10
642051366 889419386 108871643 555904199 953858856 259219146 421728989 136798930 636344083 935177053

예제 출력 2
2830129050547187
'''
