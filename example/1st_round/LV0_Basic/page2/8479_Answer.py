import sys

def limbo_check(limit:int, length_data:list) -> str:
    for length in length_data:
        if length <= limit:
            return f'I {length}'
    return 'P'

if __name__=="__main__":
    LENGTH_GUNHYUK = 160        
    read = sys.stdin.readline
    write = sys.stdout.write
    
    N = int(read())
    length_data = list(map(int, read().split()))
    
    result = limbo_check(LENGTH_GUNHYUK, length_data)    
    write(result)