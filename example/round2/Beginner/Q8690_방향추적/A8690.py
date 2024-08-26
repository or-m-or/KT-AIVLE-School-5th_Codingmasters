'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write

if __name__ == "__main__":
    N = int(readline())  # 이동 횟수
    locations = [tuple(map(int, readline().split())) for _ in range(N)]

    cur_y, cur_x = locations[0]
    for i in range(1, N):
        new_y, new_x = locations[i]

        if new_y != cur_y:
            direct = 1 if new_y > cur_y else 3
            distance = abs(new_y - cur_y)
        else:
            direct = 2 if new_x > cur_x else 4
            distance = abs(new_x - cur_x)

        write(f'{direct} {distance}\n')
        cur_y, cur_x = new_y, new_x
