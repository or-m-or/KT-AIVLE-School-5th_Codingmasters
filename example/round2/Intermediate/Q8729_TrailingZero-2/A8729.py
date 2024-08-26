'''
Type : 
'''


def trailingZeroes(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count


def solution(n):
    low, high = 0, 5 * n
    while low < high:
        mid = (low + high) // 2
        if trailingZeroes(mid) < n:
            low = mid + 1
        else:
            high = mid
    return low


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
