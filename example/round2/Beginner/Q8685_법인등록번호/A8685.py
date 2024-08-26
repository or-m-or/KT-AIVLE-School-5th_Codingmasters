'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def classify_corporation(prefix, serial, check_digit):
    # 법인 종류별 분류번호 범위 정의
    ranges = {
        '상업 법인': range(11, 16),
        '민법 법인': range(21, 23),
        '특수 법인': range(31, 52),
        '외국 법인': range(81, 87),
        '기타 법인': range(71, 72)
    }

    def calculate_check_digit(prefix, serial):
        registration_number = prefix + serial
        odd_sum = sum(int(registration_number[i]) for i in range(0, 12, 2))
        even_sum = sum(int(registration_number[i]) for i in range(1, 12, 2))
        R = (2 * even_sum + odd_sum) % 10
        return (10 - R) % 10

    # 추측할 법인 종류별 분류번호에 대해 검사 결과를 'O' 또는 'X'로 출력
    results = []
    for category, corp_range in ranges.items():
        for corp_type in corp_range:
            if calculate_check_digit(prefix, f'{corp_type:02d}' + serial) == int(check_digit):
                results.append('O')
                break
        else:
            results.append('X')

    return ''.join(results)


if __name__ == "__main__":
    # 입력 받기
    reg_num = readline().strip()  # 등기관서 4
    serial_num = readline().strip()  # 일렬번호 6
    error_num = readline().strip()  # 오류검색 1

    # 법인 종류 판별 및 출력
    result = classify_corporation(reg_num, serial_num, error_num)
    write(result + '\n')
