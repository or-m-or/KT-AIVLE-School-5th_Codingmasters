import sys

def coupon_counter(money:int) -> int:
    units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    count = 0    
    
    for unit in units:
        count += money // unit
        money %= unit
    return count

if __name__=="__main__":
    read = sys.stdin.readline
    write = sys.stdout.write
    
    money = int(read())
    count = coupon_counter(money)    
    write(str(count))