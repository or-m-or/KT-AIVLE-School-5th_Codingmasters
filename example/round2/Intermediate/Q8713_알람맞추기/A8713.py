'''
Type : 
'''
import sys

readline = sys.stdin.readline
write = sys.stdout.write


def solution(initial_time, N):
    # Parse the initial time to minutes
    initial_hours, initial_minutes = map(int, initial_time.split(':'))
    initial_total_minutes = initial_hours * 60 + initial_minutes

    # Calculate the total minutes till the N-th alarm
    if N == 1:
        # No additional minutes for the first alarm
        total_minutes = initial_total_minutes
    else:
        # Calculate the sum of the sequence of additional minutes till N-th alarm
        # S = 1 + 2 + 3 + ... + (N-1) = N(N-1)/2
        additional_minutes = (N * (N - 1) // 2)
        total_minutes = initial_total_minutes + additional_minutes

    # Adjust for 24 hour format and 60 minutes per hour
    total_hours = (total_minutes // 60) % 24
    total_minutes = total_minutes % 60

    # Return the final time in HH:MM format
    return f"{total_hours:02}:{total_minutes:02}"


if __name__ == "__main__":
    init_time = readline().strip()
    N = int(readline().strip())

    write(f'{solution(init_time, N)}\n')
