def solution(N, M, tile_counts, k, p):
    memo = {}

    def dfs(pos, last_color, k_count):
        if pos == M:
            return 1 if k_count >= p else 0

        if (pos, last_color, k_count) in memo:
            return memo[(pos, last_color, k_count)]

        total_ways = 0
        for color in range(1, N + 1):
            if tile_counts[color - 1] > 0 and abs(color - last_color) != 1:
                tile_counts[color - 1] -= 1
                total_ways += dfs(pos + 1, color, k_count + (1 if color == k else 0))
                tile_counts[color - 1] += 1

        memo[(pos, last_color, k_count)] = total_ways
        return total_ways

    total_ways = 0
    for color in range(1, N + 1):
        if tile_counts[color - 1] > 0:
            tile_counts[color - 1] -= 1
            total_ways += dfs(1, color, 1 if color == k else 0)
            tile_counts[color - 1] += 1

    return total_ways


if __name__ == "__main__":
    N, M = map(int, input().split())
    tile_counts = list(map(int, input().split()))
    k, p = map(int, input().split())
    print(solution(N, M, tile_counts, k, p))

