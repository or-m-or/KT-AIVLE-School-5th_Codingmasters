def next_permutation(arr):
    # Find the largest index k such that arr[k] < arr[k + 1]
    k = -1
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            k = i

    if k == -1:
        # If no such index exists, the permutation is the last permutation
        return sorted(arr)

    # Find the largest index l greater than k such that arr[k] < arr[l]
    l = -1
    for i in range(k + 1, len(arr)):
        if arr[k] < arr[i]:
            l = i

    # Swap the value of arr[k] with that of arr[l]
    arr[k], arr[l] = arr[l], arr[k]

    # Reverse the sequence from arr[k + 1] up to and including the final element arr[n]
    arr = arr[:k + 1] + arr[k + 1:][::-1]
    
    return arr

def solution(N, K, perm):
    for _ in range(K):
        perm = next_permutation(perm)
    return perm

if __name__ == "__main__":
    N, K = map(int, input().split())
    perm = list(map(int, input().split()))
    result = solution(N, K, perm)
    print(" ".join(map(str, result)))
