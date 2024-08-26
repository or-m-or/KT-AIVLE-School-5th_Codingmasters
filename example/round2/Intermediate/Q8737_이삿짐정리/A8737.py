'''
Type : 
'''


def solution(init_state):
    case = {'RGB', 'GBR', 'BRG'}
    if init_state in case:
        return "possible"
    else:
        return "impossible"


if __name__ == "__main__":
    state = input()
    print(solution(state))


# 통과한 코드
# import sys

# state = input()

# if state == 'R G B':
#     print('possible')
# elif state == 'R B G':
#     print('impossible')
# elif state == 'B R G':
#     print('possible')
# elif state == 'B G R':
#     print('impossible')
# elif state == 'G B R':
#     print('possible')
# elif state == 'G R B':
#     print('impossible')
