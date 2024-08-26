import sys

readline = sys.stdin.readline
write = sys.stdout.write

if __name__=="__main__":
    N = int(readline())
    K = sorted(list(map(int, readline().split())), reverse=True)
    
    max_score = 0
    for i, score in enumerate(K):
        current_score = score * (i+1) 
        if max_score < current_score:
            max_score = current_score
    
    write(str(max_score)+'\n')
    