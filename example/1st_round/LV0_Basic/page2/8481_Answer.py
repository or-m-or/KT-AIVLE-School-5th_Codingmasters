import sys
from operator import itemgetter

if __name__=="__main__":
    read = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(read())
    students = {}
    for _ in range(N):
        name, iq = read().split()
        students[f'{name}'] = int(iq)   
    
    # items() -> key, value 순서로 반환
    sorted_names = sorted(students.items(), key=itemgetter(1), reverse=True)[0:3]
    for name, _ in sorted_names:
        write(name+'\n')
        
    
"""
1. lambda를 이용한 딕셔너리 정렬 방식(값기준)

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

2. operator 의 itemgetter을 이용한 딕셔너리 정렬 방식

from operator import itemgetter

sorted_dict = dict(sorted(my_dict.items(), key=itemgetter(1)))
"""