import sys

if __name__=="__main__":
    read = sys.stdin.readline
    write = sys.stdout.write
    
    angle1, angle2, angle3 = map(int, read().split())
    answer = 'P' if (angle1 + angle2 + angle3) == 180 else 'F'
    write(answer)