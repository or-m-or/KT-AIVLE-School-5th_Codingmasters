'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write

if __name__ == "__main__":
    N, M = map(int, readline().split())  # 컵 수, 섞은 횟수
    moves = [tuple(map(int, readline().split())) for _ in range(M)]
    K = int(readline())  # 처음 공 위치

    location = [False] * (N+1)
    location[K] = True

    for A, B in moves:
        if location[A] == True or location[B] == True:
            location[A] = not location[A]
            location[B] = not location[B]

    for i in range(1, N+1):
        if location[i] == True:
            write(f'{i}\n')
            break
