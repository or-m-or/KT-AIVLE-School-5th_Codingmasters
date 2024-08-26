'''
Type : 
'''


def calc_vat2(total):
    # 가능한 최소 공급가액 계산 (부가가치세가 최대인 경우 고려)
    min_supply = int(total / 1.1)
    # 가능한 최대 공급가액 계산
    max_supply = total

    # 가능한 공급가액 범위 내에서 공급가액과 부가가치세 계산
    for supply in range(min_supply, max_supply + 1):
        vat = supply // 10
        # 계산된 부가가치세와 공급가액의 합이 총액과 일치하는지 확인
        if supply + vat == total:
            return supply, vat

    # 조건을 만족하는 공급가액과 부가가치세를 찾지 못한 경우
    return -1


if __name__ == "__main__":
    total = int(input())

    supply_price, vat = calc_vat2(total)
    if supply_price == -1:
        print(-1)
    else:
        print(supply_price, vat)
