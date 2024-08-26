'''
Type : 
'''

def solution(encoded):
    decoded = []
    i = len(encoded)-1
    while i > -1:
        if encoded[i] == '0':
            number = int(encoded[i-2: i])
            decoded.append(chr(number + ord('a') -1))
            i -= 3
        else:
            number = int(encoded[i])
            decoded.append(chr(number + ord('a') -1))
            i -= 1

    ans = ''
    for _ in range(len(decoded)):
        ans += decoded.pop()
    return ans            


if __name__ == "__main__":
    text = input().strip()
    print(solution(text))
