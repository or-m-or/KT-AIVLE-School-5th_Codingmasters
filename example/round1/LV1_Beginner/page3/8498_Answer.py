import sys

read = sys.stdin.readline
write = sys.stdout.write

board = [[(i+j) % 2 for j in range(8)] for i in range(8)]
moles = [list(read().strip()) for _ in range(8)]

count = 0
for i in range(8):
    for j in range(8):
        if moles[i][j] == 'F' and board[i][j] == 0:
            count += 1

write(str(count))