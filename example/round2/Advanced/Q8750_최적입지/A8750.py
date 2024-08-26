def get_distance_sum(position, houses):
    distance_sum = 0
    for i in range(len(houses)):
        distance_sum += abs(i - position) * houses[i]
    return distance_sum

def solution(N, grid):
    # Step 1: Collect house coordinates
    houses = []
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 'H':
                houses.append((r, c))

    # Step 2: Calculate row and column house counts
    row_houses = [0] * N
    col_houses = [0] * N
    for r, c in houses:
        row_houses[r] += 1
        col_houses[c] += 1

    min_distance_sum = float('inf')
    optimal_location = None

    # Step 4: Calculate distance sum for each cell
    for r in range(N):
        row_distance_sum = get_distance_sum(r, row_houses)
        for c in range(N):
            col_distance_sum = get_distance_sum(c, col_houses)
            total_distance_sum = row_distance_sum + col_distance_sum
            if total_distance_sum < min_distance_sum:
                min_distance_sum = total_distance_sum
                optimal_location = (r + 1, c + 1)  # convert to 1-based index
            elif total_distance_sum == min_distance_sum:
                if (r + 1, c + 1) < optimal_location:
                    optimal_location = (r + 1, c + 1)

    return optimal_location


if __name__ == "__main__":
    N = int(input())
    grid = [input().strip() for _ in range(N)]
    result = solution(N, grid)
    print(result[0], result[1])
