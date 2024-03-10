import sys

if __name__=="__main__":
    read = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(read())
    num1 = N % 5
    num2 = N % 7
    
    ans = num2 if num1 < num2 else num1
    write(str(ans))