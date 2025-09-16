def bfs(idx, cnt):
    if cnt == N // 2:
        return
    

    for i in range(idx, N):
        visited[idx] = True
        bfs(i + 1, cnt + 1)
        visited[idx] = False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    visited = [False] * N

    synerge_table = []
    for _ in range(N):
        row = list(map(int, input().split()))
        synerge_table.append(row)
    
