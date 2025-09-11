def recur(row):
    global pay, result
    if row == N:
        if pay < result:
            result = pay
        return
    
    # pruning
    if pay >= result:
        return
    
    for col in range(N):
        if not visited[col]:
            # 방문처리
            visited[col] = True
            pay += prices[row][col]
            # 재귀호출
            recur(row + 1)
            # 백트래킹
            pay -= prices[row][col]
            visited[col] = False
        
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    prices = []
    for _ in range(N):
        row = list(map(int, input().split()))
        prices.append(row)

    visited = [False] * N
    pay = 0
    result = float('inf')

    recur(0)
    print(f'#{test_case} {result}')