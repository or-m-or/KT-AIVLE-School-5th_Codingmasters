import sys

'''
솔루션1
''' 
def solution1(number: int) -> int:    
    octo_num = ''
    hexa_num = ''
    dici_to_hexa = {
        '10':'A',
        '11':'B',
        '12':'C',
        '13':'D',
        '14':'E',
        '15':'F',
        '16':'G'
    }

    deci_num = number
    while(deci_num > 0):
        octo_num = str(deci_num % 8) + octo_num
        deci_num = deci_num//8

    deci_num = number
    while(deci_num > 0):
        hexa_digit = str(deci_num % 16)
        if hexa_digit in dici_to_hexa:
            hexa_digit = dici_to_hexa[hexa_digit]
        hexa_num = hexa_digit + hexa_num
        deci_num = deci_num//16

    return octo_num, hexa_num
    

'''
솔루션2 : 실행속도 최적화
1. 내장 함수 사용
2. 기능별 함수 분리
'''    
def solution2(number: int) -> str:
    octo_num = oct(number)[2:]
    hexa_num = hex(number)[2:].upper()
    return octo_num,  hexa_num

if __name__=="__main__":
    read = sys.stdin.readline
    number = int(read())
    answer1, answer2 = solution2(number)
    sys.stdout.write(answer1+' '+answer2)