def is_valid_connection(N, M, K, connection_record):
    def get_hub(computer):
        if computer == 0:
            return -1  # 중앙 컴퓨터
        return (computer - 1) // M + 1

    for i in range(1, K):
        prev = connection_record[i-1]
        curr = connection_record[i]
        prev_hub = get_hub(prev)
        curr_hub = get_hub(curr)

        if prev == 0 or curr == 0:
            # 한쪽이 중앙 컴퓨터일 경우, 다른 쪽은 허브여야 한다
            if prev != 0 and (prev % M != 1):
                return "NO"
            if curr != 0 and (curr % M != 1):
                return "NO"
        else:
            # 둘 다 중앙 컴퓨터가 아닌 경우, 같은 허브에 있어야 한다
            if prev_hub != curr_hub:
                return "NO"
    
    return "YES"

if __name__=="__main__":
    N, M = map(int, input().split())
    K = int(input().strip())
    connection_record = list(map(int, input().split()))
    print(is_valid_connection(N, M, K, connection_record))  
