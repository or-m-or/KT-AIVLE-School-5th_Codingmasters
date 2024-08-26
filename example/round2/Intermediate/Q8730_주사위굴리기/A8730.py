'''
Type : 
'''
def solution(W:int, H:int, X:int, Y:int, dice:list, roll:list) -> list:

    ground = [[0] * W for _ in range(H)]
    ground[Y][X] = dice[5] 
    
    # E, S, W, N 순서 - (Y, X)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    cur_y, cur_x = Y, X
    for cur_dir in roll:
        temp_y, temp_x = cur_y, cur_x
        if cur_dir == 1: # East
            # 현재 위치 업데이트
            temp_y += directions[0][0]
            temp_x += directions[0][1]
            # 주사위 업데이트
            dice[5], dice[4], dice[0], dice[2] = dice[0], dice[2], dice[4], dice[5]
                        
        elif cur_dir == 2: # South
            temp_y += directions[1][0]
            temp_x += directions[1][1]
            dice[5], dice[4], dice[1], dice[3] = dice[1], dice[3], dice[4], dice[5]
            
        elif cur_dir == 3: # West
            temp_y += directions[2][0]
            temp_x += directions[2][1]
            dice[4], dice[5], dice[2], dice[0] = dice[0], dice[2], dice[4], dice[5]
                        
        elif cur_dir == 4: # North
            temp_y += directions[3][0]
            temp_x += directions[3][1]
            dice[4], dice[5], dice[3], dice[1] = dice[1], dice[3], dice[4], dice[5]
            
        # 바닥면에 기록
        if -1< temp_x < W and -1< temp_y < H:
            cur_y, cur_x = temp_y, temp_x
            ground[temp_y][temp_x] = dice[5]
        else:
            ground[cur_y][cur_x] = dice[5]
    
    return ground
    
    

if __name__ == "__main__":
    W, H = map(int, input().split())
    X, Y = map(int, input().split())
    dice = list(map(int, input().split()))
    N = int(input())
    roll = list(map(int, input().split()))
    
    ans = solution(W, H, X, Y, dice, roll)
    for item in ans:
        print(*item, sep=' ')