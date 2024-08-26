import sys
from datetime import datetime

readline = sys.stdin.readline
write = sys.stdout.write

length = int(readline())
N = int(readline())

date_format = "%H:%M:%S"
start_log = []
end_log = []
for _ in range(N):
    num_log, time_log = readline().strip().split()
    time_log = datetime.strptime(time_log, date_format)
    start_log.append([num_log, time_log])

for _ in range(N):
    num_log, time_log = readline().strip().split()
    time_log = datetime.strptime(time_log, date_format)
    end_log.append([num_log, time_log])

start_log.sort()
end_log.sort()

for i in range(N):
    time_diff = end_log[i][1] - start_log[i][1]
    time_hour = time_diff.total_seconds() / 3600
    speed = length / time_hour
    write(f'{start_log[i][0]} {int(speed)}\n')