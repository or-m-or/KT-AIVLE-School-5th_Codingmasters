import sys

readline = sys.stdin.readline
write = sys.stdout.write

data = readline().strip()

length_count_gap = len(data)
length_nocount_gap = 0
length_word = 1
for i in range(len(data)):
    if data[i] != ' ':
        length_nocount_gap += 1
    elif data[i] == ' ' and data[i+1] != ' ':
        length_word += 1
        
write(f'{length_count_gap}\n{length_nocount_gap}\n{length_word}\n')