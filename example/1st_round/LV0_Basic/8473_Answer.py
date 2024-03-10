import sys

if __name__=="__main__":
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    write('P' if len(readline()) < 21 else 'I')