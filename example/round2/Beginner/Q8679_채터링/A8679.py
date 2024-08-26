import sys

readline = sys.stdin.readline
write = sys.stdout.write

if __name__ == "__main__":
    N, K = map(int, readline().split())
    text = readline().rstrip()
    ans = ''
    for char in text:
        ans += char * K

    write(ans+'\n')
