def is_left(P0, P1, P2):
    return (P1[0] - P0[0]) * (P2[1] - P0[1]) - (P2[0] - P0[0]) * (P1[1] - P0[1])


def winding_number(P, V):
    wn = 0
    n = len(V)
    for i in range(n):
        if V[i][1] <= P[1]:
            if V[(i + 1) % n][1] > P[1]:
                if is_left(V[i], V[(i + 1) % n], P) > 0:
                    wn += 1
        else:
            if V[(i + 1) % n][1] <= P[1]:
                if is_left(V[i], V[(i + 1) % n], P) < 0:
                    wn -= 1
    return wn


def solution(N, M, polygon_points, test_points):
    polygon = [(polygon_points[2 * i], polygon_points[2 * i + 1]) for i in range(N)]
    points = [(test_points[2 * i], test_points[2 * i + 1]) for i in range(M)]

    for point in points:
        if winding_number(point, polygon) == 0:
            return "NO"
    return "YES"


if __name__ == "__main__":
    N, M = map(int, input().split())
    polygon_points = list(map(int, input().split()))
    test_points = list(map(int, input().split()))

    print(solution(N, M, polygon_points, test_points))
