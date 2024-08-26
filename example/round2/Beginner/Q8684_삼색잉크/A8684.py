'''
Type : 구현
'''
import sys


readline = sys.stdin.readline


class CalendarColorCounter:
    def __init__(self, start_day):
        self.start_day = start_day
        self.day_to_num = {"SUN": 0, "MON": 1, "TUE": 2,
                           "WED": 3, "THU": 4, "FRI": 5, "SAT": 6}
        self.days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.red_count = [0] * 10
        self.blue_count = [0] * 10
        self.black_count = [0] * 10
        self.start_day_num = self.day_to_num[self.start_day]

    def calculate_day(self, month: int, day: int) -> int:
        ''' 입력 받은 날짜의 요일을 계산하는 메서드 '''
        total_days = sum(self.days_in_month[:month-1]) + day - 1
        return (total_days + self.start_day_num) % 7

    def count_number(self, day, color_count):
        ''' 각 날짜(일자)에 사용된 숫자 개수 계산하는 메서드 '''
        for digit in str(day):
            color_count[int(digit)] += 1

    def process_dates(self, holidays):
        ''' 각 일자 별 잉크 사용 횟수 계산하는 메서드 '''
        for month in range(1, 13):
            for day in range(1, self.days_in_month[month-1] + 1):
                day_num = self.calculate_day(month, day)     # 날짜 -> 요일
                if (month, day) in holidays or day_num == 0:  # 빨간색
                    self.count_number(day, self.red_count)
                elif day_num == 6:                           # 파란색
                    self.count_number(day, self.blue_count)
                else:                                        # 검은색
                    self.count_number(day, self.black_count)

    def print_counts(self):
        ''' 최종 결과값 화면에 출력하는 메서드 '''
        for i in range(10):
            print(self.red_count[i], self.blue_count[i], self.black_count[i])


if __name__ == "__main__":
    start_day = readline().strip()
    N = int(readline().strip())
    holidays = [tuple(map(int, readline().split())) for _ in range(N)]

    counter = CalendarColorCounter(start_day)
    counter.process_dates(holidays)
    counter.print_counts()
