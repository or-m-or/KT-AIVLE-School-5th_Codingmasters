'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def find_max_children(n, gifts):
    max_children = gifts[0]
    for i in range(1, n):
        max_children = gcd(max_children, gifts[i])
    return max_children


if __name__ == "__main__":
    N = int(readline())
    gifts = list(map(int, readline().split()))

    ans = find_max_children(N, gifts)
    write(str(ans)+'\n')
