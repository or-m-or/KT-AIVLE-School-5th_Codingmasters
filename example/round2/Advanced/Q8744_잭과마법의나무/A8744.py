from collections import deque


def min_days_to_reach_height(N):
    if N == 1:
        return 0  # If the target height is 1, it is already at 1 at day 0

    queue = deque([(1, 1, 0)])  # (height, previous height, days)
    visited = set((1, 1))

    while queue:
        height, prev_height, days = queue.popleft()

        # Calculate the next heights based on the three weather conditions
        # Sunny day
        new_height_sunny = height + prev_height
        if new_height_sunny == N:
            return days + 1
        if (new_height_sunny, height) not in visited:
            visited.add((new_height_sunny, height))
            queue.append((new_height_sunny, height, days + 1))

        # Cloudy day
        new_height_cloudy = max(1, height - 1)
        if new_height_cloudy == N:
            return days + 1
        if (new_height_cloudy, height) not in visited:
            visited.add((new_height_cloudy, height))
            queue.append((new_height_cloudy, height, days + 1))

        # Stormy day
        new_height_stormy = (prev_height + height) // 2
        if new_height_stormy == N:
            return days + 1
        if (new_height_stormy, height) not in visited:
            visited.add((new_height_stormy, height))
            queue.append((new_height_stormy, height, days + 1))

    return -1  # In case the target height N cannot be reached


if __name__ == '__main__':
    T = int(input())
    results = []

    for _ in range(T):
        N = int(input())
        results.append(min_days_to_reach_height(N))

    # Output results
    for result in results:
        print(result)
