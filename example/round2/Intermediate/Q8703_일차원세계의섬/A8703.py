'''
Type : 
'''


def count_islands(map_str):
    count = 0
    in_island = False
    for ch in map_str:
        if ch == 'g':
            if not in_island:
                count += 1
                in_island = True
        else:
            in_island = False
    return count


def solution(map_str):
    n = len(map_str)
    min_map = list(map_str)
    max_map = list(map_str)

    # 최소 섬 개수를 위한 맵 변환
    i = 0
    while i < n:
        if min_map[i] == 'x':
            if (i > 0 and min_map[i-1] == 'g') or (i < n-1 and min_map[i+1] == 'g'):
                min_map[i] = 'g'
            else:
                min_map[i] = 'o'
        i += 1

    # 최대 섬 개수를 위한 맵 변환
    i = 0
    while i < n:
        if max_map[i] == 'x':
            start = i
            while i < n and max_map[i] == 'x':
                i += 1
            length = i - start
            left = max_map[start-1] if start > 0 else 'o'
            right = max_map[i] if i < n else 'o'

            fill_char = 'g' if left == 'o' else 'o'
            for j in range(start, i):
                max_map[j] = fill_char
                fill_char = 'o' if fill_char == 'g' else 'g'
            continue
        i += 1

    min_islands = count_islands(''.join(min_map))
    max_islands = count_islands(''.join(max_map))

    return min_islands, max_islands


if __name__ == "__main__":
    maps = input().strip()
    min_islands, max_islands = solution(maps)

    print(f'{min_islands}\n{max_islands}')
