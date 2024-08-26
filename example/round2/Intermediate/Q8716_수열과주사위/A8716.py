def dice_prob():
    # 주사위 합의 확률 계산
    probabilities = {sum_value: 0 for sum_value in range(3, 19)}
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                sum_value = i + j + k
                probabilities[sum_value] += 1

    total_cases = 6 * 6 * 6
    probabilities = {key: value / total_cases for key, value in probabilities.items()}

    return probabilities

def solution(N, scores, prob):
    max_expected_value = float('-inf')
    best_ks = []

    for K in range(1, N + 1):
        expected_value = 0
        
        for T in range(3, 19):
            index = K + T - 1
            if index >= N:
                score = -100
            else:
                score = scores[index]
            expected_value += prob[T] * score
        
        final_expected_value = round(expected_value * 216)

        if final_expected_value > max_expected_value:
            max_expected_value = final_expected_value
            best_ks = [K]
        elif final_expected_value == max_expected_value:
            best_ks.append(K)
        

    return max_expected_value, best_ks


if __name__ == "__main__":    
    N = int(input().strip())
    scores = list(map(int, input().strip().split()))
    prob = dice_prob()
    max_expected_value, best_ks = solution(N, scores, prob)
    print(int(max_expected_value))
    print(" ".join(map(str, best_ks)))


# 케이스 1	Passed	1.418 s
# 케이스 2	Passed	1.434 s
# 케이스 3	Passed	1.956 s
# 케이스 4	Passed	1.889 s
# 케이스 5	Failed	2.236 s
# 케이스 6	Passed	2.166 s
# 케이스 7	Passed	1.412 s