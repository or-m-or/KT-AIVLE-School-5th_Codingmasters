import sys

if __name__=="__main__":
    read = sys.stdin.readline
    write = sys.stdout.write
    
    mom_height, dad_height = map(int, read().split())    
    write(str((mom_height+dad_height) // 2))