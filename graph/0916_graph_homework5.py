from heapq import heappush, heappop
def dijkstra(board):
    N = len(board)
    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]    # cost, r, c

    # delta
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while pq:
        cost, r, c = heappop(pq)
        
        if cost > dist[r][c]:
            continue
        if r == N - 1 and c == N - 1:
            return cost
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                extra = max(0, board[nr][nc] - board[r][c])
                ncost = cost + 1 + extra
                if ncost < dist[nr][nc]:
                    dist[nr][nc] = ncost
                    heappush(pq, (ncost, nr, nc))

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = dijkstra(board)
    print(f'#{test_case} {result}')
