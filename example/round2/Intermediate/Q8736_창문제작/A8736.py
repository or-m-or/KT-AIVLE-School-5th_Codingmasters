
# from collections import deque


# def min_transactions(N, a, b):
#     queue = deque([(1, 0)])
#     visited = set([(1, 0)])
#     transactions = 0

#     while queue:
#         for _ in range(len(queue)):
#             frames, glasses = queue.popleft()

#             if frames >= N and glasses >= N:
#                 return transactions

#             new_frames_1 = frames - 1 + a
#             new_glasses_1 = glasses
#             if (new_frames_1, new_glasses_1) not in visited:
#                 visited.add((new_frames_1, new_glasses_1))
#                 queue.append((new_frames_1, new_glasses_1))

#             if frames >= b:
#                 new_frames_2 = frames - b
#                 new_glasses_2 = glasses + 1
#                 if (new_frames_2, new_glasses_2) not in visited:
#                     visited.add((new_frames_2, new_glasses_2))
#                     queue.append((new_frames_2, new_glasses_2))

#         transactions += 1

#     return -1


# N, a, b = map(int, input().split())
# print(min_transactions(N, a, b))

#
# 케이스 1	Passed	1.427 s
# 케이스 2	Failed	30.001 s	Timeout
# 케이스 3	Failed	30 s	Timeout
# 케이스 4	Passed	1.394 s
# 케이스 5	Passed	1.228 s
# 케이스 6	Failed	30 s	Timeout
# 케이스 7	Passed	1.194 s



def solution(N, a, b):
    total_frames = N * (1 + b)
    add_frames = total_frames - 1
 
    get_prames = (add_frames + (a - 2)) // (a - 1) if a > 1 else add_frames
    total_transactions = get_prames + N
    return total_transactions

if __name__ == "__main__":
    N, a, b = map(int, input().split())
    print(solution(N, a, b))