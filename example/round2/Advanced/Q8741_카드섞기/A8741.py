'''
Type : 
'''
def find_cycle_length(perm):
    N = len(perm)
    visited = [False] * N
    cycle_length = [0] * N

    for i in range(N):
        if not visited[i]:
            current = i
            cycle = []
            while not visited[current]:
                visited[current] = True
                cycle.append(current)
                current = perm[current] - 1
            length = len(cycle)
            for node in cycle:
                cycle_length[node] = length
    return cycle_length


# def apply_permutation(perm, k):
#     N = len(perm)
#     result = list(range(1, N + 1))
#     for _ in range(k):
#         new_result = [0] * N
#         for i in range(N):
#             new_result[perm[i] - 1] = result[i]
#         result = new_result
#     return result


if __name__ == "__main__":

    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    

    cycle_length = find_cycle_length(A)
    result = list(range(1, N + 1))
    for i in range(N):
        effective_k = K % cycle_length[i]
        current_pos = i
        for _ in range(effective_k):
            current_pos = A[current_pos] - 1
        result[current_pos] = i + 1

    print(" ".join(map(str, result)))





