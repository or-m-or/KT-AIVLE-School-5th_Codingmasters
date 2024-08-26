'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def calculate_satisfaction(incinerator_pos):
    satisfaction = 0
    for house in houses:
        d = abs(incinerator_pos - house)
        if d <= k:
            satisfaction += d
        else:
            satisfaction -= d
    return satisfaction


if __name__ == "__main__":
    n, k = map(int, readline().split())
    houses = list(map(int, readline().split()))

    max_satisfaction = float('-inf')
    best_position = None

    for pos in houses:
        curr_satisfaction = calculate_satisfaction(pos)
        if curr_satisfaction > max_satisfaction:
            max_satisfaction = curr_satisfaction
            best_position = pos

    write(f'{best_position}\n')
