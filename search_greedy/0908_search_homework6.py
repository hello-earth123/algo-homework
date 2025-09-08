T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    time_table = []
    for _ in range(N):
        start_end = list(map(int, input().split()))
        time_table.append(start_end)
    # 회의가 빨리 끝나는 시점을 기준으로 정렬
    time_table.sort(key = lambda x : x[1])
    # print(time_table)
    cnt = 1
    end_time = time_table[0][1]
    for i in range(1, len(time_table)):
        start_time = time_table[i][0]
        if end_time <= start_time:
            cnt += 1
            end_time = time_table[i][1]
    
    print(f'#{test_case} {cnt}')        
        