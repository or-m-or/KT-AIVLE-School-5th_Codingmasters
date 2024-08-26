def is_palindromic_time(hour, minute):
    ''' HH:MM 형식이 주어질 때, 앞뒤로 뒤집어도 같은 시각인지 확인 '''
    hour_str = f"{hour:02}"
    minute_str = f"{minute:02}"
    time_str = hour_str + minute_str
    return time_str == time_str[::-1]

def solution(start_time, k):
    start_hour, start_minute = map(int, start_time.split(':'))
    current_minutes = start_hour * 60 + start_minute
    palindromic_count = 0
    seen_times = set()

    for _ in range(1440):  
        hour = (current_minutes // 60) % 24
        minute = current_minutes % 60

        if (hour, minute) in seen_times:
            break
        seen_times.add((hour, minute))
        
        if is_palindromic_time(hour, minute):
            palindromic_count += 1
        
        current_minutes += k
    return palindromic_count


if __name__ == "__main__":
    time = input().strip()
    k = int(input().strip())
    result = solution(time, k)
    print(result)
