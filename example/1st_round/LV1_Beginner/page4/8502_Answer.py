import sys

def find_seconds_with_N(N):
    total_seconds = 0

    for hour in range(24):
        for minute in range(60):
            for second in range(60):
                if str(N) in f"{hour:02d}{minute:02d}{second:02d}":
                    total_seconds += 1
    return total_seconds


if __name__=="__main__":
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(readline())
    write(str(find_seconds_with_N(N)))


'''
[Python] 리스트에서 같은 값을 빼는 법

1. numpy 이용

a = [1,2,3]
output = np.subtract(a, 1)
print(output)
[0 1 2]
 

2.List Comprehension 이용

a = [1,2,3]
output1 = [i-1 for i in a]
print(output1)
# [0, 1, 2]


3. map 이용

output2 = list(map(lambda x:x -1, a))
print(output2)
# [0, 1, 2]

'''