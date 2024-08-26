'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def hex_to_gray(hex_code):
    # 헥스 코드에서 R, G, B 값을 분리
    r = int(hex_code[1:3], 16)
    g = int(hex_code[3:5], 16)
    b = int(hex_code[5:], 16)

    # R, G, B의 평균을 계산
    avg = round((r + g + b) / 3)

    # 헥스 코드로 변환
    gray_hex = '#{:02X}{:02X}{:02X}'.format(avg, avg, avg)

    return gray_hex


if __name__ == "__main__":
    hex_code = readline().strip()
    write(f'{hex_to_gray(hex_code)}')
