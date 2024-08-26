def dfs(start):
    visited[start] = True
    group_info = {
        'size': 1,
        'min_id': start
    }

    for next in graph[start]:
        if not visited[next]:
            visited[next] = True
            next_group_info = dfs(next)
            group_info['size'] += next_group_info['size']
            group_info['min_id'] = min(
                group_info['min_id'], next_group_info['min_id'])
    return group_info


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    max_group = {'size': 0, 'min_id': n + 1}
    for i in range(1, n + 1):
        if not visited[i]:
            current_group = dfs(i)
            if current_group['size'] > max_group['size'] or \
                    (current_group['size'] == max_group['size'] and
                        current_group['min_id'] < max_group['min_id']):
                max_group = current_group

    print(max_group['min_id'])
