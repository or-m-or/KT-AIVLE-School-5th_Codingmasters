def calculate_minimum_tiles(N, K, M, rain_data):
    # Initialize the rain_count matrix
    rain_count = [[0] * N for _ in range(N)]

    # Update rain_count matrix with rain information
    for data in rain_data:
        X, Y, Z, W = data
        for i in range(X - 1, Z):
            for j in range(Y - 1, W):
                rain_count[i][j] += 1

    # Calculate the number of tiles needed to replace
    total_replacements = 0
    for i in range(N):
        for j in range(N):
            if rain_count[i][j] > 0:
                total_replacements += rain_count[i][j] // K

    return total_replacements


# Input reading
N = int(input())
K = int(input())
M = int(input())
rain_data = [tuple(map(int, input().split())) for _ in range(M)]

# Calculate and print the result
result = calculate_minimum_tiles(N, K, M, rain_data)
print(result)
