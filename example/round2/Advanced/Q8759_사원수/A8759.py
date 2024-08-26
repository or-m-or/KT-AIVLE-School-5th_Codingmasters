def solution(q1, q2):
    a, b, c, d = q1
    w, x, y, z = q2

    o = a * w - b * x - c * y - d * z
    p = a * x + b * w + c * z - d * y
    q = a * y - b * z + c * w + d * x
    r = a * z + b * y - c * x + d * w

    return o, p, q, r


if __name__ == "__main__":
    q1 = list(map(int, input().split()))
    q2 = list(map(int, input().split()))
    result = solution(q1, q2)
    print(" ".join(map(str, result)))
