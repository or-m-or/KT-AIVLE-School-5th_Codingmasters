"""
TYPE : 플로이드-와샬
"""
def find_bus_routes(n, adjacency_matrix):
    # Initialize the result matrix with the input adjacency matrix
    result = [row[:] for row in adjacency_matrix]

    # Apply Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if result[i][j] or (result[i][k] and result[k][j]):
                    result[i][j] = 1

    return result


if __name__ == "__main__":
    n = int(input().strip())
    matrix = [ list(map(int, input().strip().split())) for _ in range(n)] 
    result_matrix = find_bus_routes(n, matrix)
    for row in result_matrix:
        print(' '.join(map(str, row)))
