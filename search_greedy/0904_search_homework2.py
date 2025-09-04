T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    plate = []
    for _ in range(N):
        row = list(map(int, input().split()))
        plate.append(row)


    result = float('inf')
    def my_sum(r, c, total):
        global result

        # 가지치기
        if total >= result:
            return

        # 종료 조건
        if r == N - 1 and c == N - 1:  
            result = min(result, total + plate[r][c])
            return

        #delta
        dr = [0, 1]
        dc = [1, 0]
        
        # 우, 하 중에 더 작은 곳으로 간다
        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < N:
                my_sum(nr, nc, total + plate[r][c])

    my_sum(0, 0, 0)
    print(f'#{test_case} {result}')
