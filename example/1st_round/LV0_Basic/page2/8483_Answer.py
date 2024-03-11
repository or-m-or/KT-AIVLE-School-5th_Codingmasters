import sys

read = sys.stdin.readline
write = sys.stdout.write

query = read().strip()

if query == "You":
    write('Me')
else:
    write('No')