import sys

def cow_ranker(weight:int) -> str:
    if weight >= 200:
        return 'A'
    elif weight >= 180:
        return 'B'
    elif weight >= 150:
        return 'C'
    else:
        return 'D'


if __name__=="__main__":
    read = sys.stdin.readline
    write = sys.stdout.write
    
    weight = int(read())    
    rank = cow_ranker(weight=weight)    
    write(rank)