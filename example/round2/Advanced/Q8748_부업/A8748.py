def can_pack_exactly(N, K, a1, a2, b1, b2):
    if a1 != 0 and a2 != 0:
        if N % a1 == 0 and K % a2 == 0 and (N // a1) == (K // a2):
            return True

    if b1 != 0 and b2 != 0:
        if N % b1 == 0 and K % b2 == 0 and (N // b1) == (K // b2):
            return True

    for x in range(51):
        for y in range(51):
            if a1 * x + b1 * y == N and a2 * x + b2 * y == K:
                return True
    return False


if __name__ == "__main__":
    T = int(input().strip())
    results = []

    for _ in range(T):
        N, K = map(int, input().strip().split())
        a1, a2 = map(int, input().strip().split())
        b1, b2 = map(int, input().strip().split())

        if can_pack_exactly(N, K, a1, a2, b1, b2):
            results.append("YES")
        else:
            results.append("NO")

    for result in results:
        print(result)
