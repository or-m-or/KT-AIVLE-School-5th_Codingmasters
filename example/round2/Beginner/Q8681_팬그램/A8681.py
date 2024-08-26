import sys

readline = sys.stdin.readline
write = sys.stdout.write

if __name__ == "__main__":
    text = readline().rstrip().lower()
    text_set = set(text)

    text = ''.join(text_set)

    if len(text) == 26:
        write('YES\n')
    else:
        write('NO\n')
