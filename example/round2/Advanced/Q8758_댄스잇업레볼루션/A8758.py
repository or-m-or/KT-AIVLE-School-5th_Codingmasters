# # 입력값 받기
# n = int(input().strip())
# pattern = list(map(int, input().strip().split()))

# # 각도 테이블 정의
# sight_angle = {
#     (1, 2): 45, (1, 3): -45, (1, 4): 0,
#     (2, 1): -135, (2, 3): -90, (2, 4): -45,
#     (3, 1): 135, (3, 2): 90, (3, 4): 45,
#     (4, 1): 180, (4, 2): 135, (4, 3): -135
# }

# # 각도 변화 검사 함수
# def can_alternate(pattern, start_left):
#     foot = ['0', '0']
#     is_left = start_left
#     last_angle = None
    
#     for p in pattern:
#         if is_left:
#             foot[0] = p
#         else:
#             foot[1] = p
#         is_left = not is_left

#         if '0' not in foot:
#             current_angle = sight_angle[(foot[0], foot[1])]
#             if last_angle is not None:
#                 angle_diff = abs(last_angle - current_angle)
#                 if angle_diff > 180:
#                     return False
#             last_angle = current_angle
#     return True

# # 왼발로 시작할 때와 오른발로 시작할 때를 모두 검사
# if can_alternate(pattern, True) or can_alternate(pattern, False):
#     print("OK")
# else:
#     print("NG")



def define_sight_angle():
    """
    각도 테이블을 정의하는 함수
    """
    return {
        (1, 2): 45, (1, 3): -45, (1, 4): 0,
        (2, 1): -135, (2, 3): -90, (2, 4): -45,
        (3, 1): 135, (3, 2): 90, (3, 4): 45,
        (4, 1): 180, (4, 2): 135, (4, 3): -135
    }

def can_alternate(pattern, start_left, sight_angle):
    """
    각도 변화 검사를 통해 패턴이 유효한지 확인하는 함수
    """
    foot = ['0', '0']
    is_left = start_left
    last_angle = None
    
    for p in pattern:
        if is_left:
            foot[0] = p
        else:
            foot[1] = p
        is_left = not is_left

        if '0' not in foot:
            current_angle = sight_angle[(foot[0], foot[1])]
            if last_angle is not None:
                angle_diff = abs(last_angle - current_angle)
                if angle_diff > 180:
                    return False
            last_angle = current_angle
    return True


if __name__ == "__main__":
    n = int(input().strip())
    pattern = list(map(int, input().strip().split()))

    sight_angle = define_sight_angle()
    if can_alternate(pattern, True, sight_angle) or can_alternate(pattern, False, sight_angle):
        print("OK")
    else:
        print("NG")
    
