'''
Type : 
'''


def money_game(N, M):

    while True:
        if N == 0 or M == 0:
            break
        elif N >= 2 * M:
            N = N % (M * 2)
        elif M >= 2 * N:
            M = M % (N * 2)
        else:
            break
    return N, M


if __name__ == "__main__":
    N, M = map(int, input().split())
    result = money_game(N, M)
    print(result[0], result[1])
