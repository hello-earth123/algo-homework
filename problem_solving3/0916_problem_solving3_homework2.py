# 파손되었으면 지나갈 수 없다.
# 깊이 == 복구 시간 == 비용으로 치환
from heapq import heappush, heappop
def dijkstra(start_row, start_col):
    pq = [(0, start_row, start_col)]  # 비용, 시작점
    costs = [[float('inf')] * N for _ in range(N)]  # 비용이 무한대라고 가정
    costs[start_row][start_col] = 0       # 첫 번째는 비용 0

    # delta
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while pq:
        cost, r, c = heappop(pq)
        if costs[r][c] < cost:
            continue
        
        # 마지막에 도착하면 cost 반환
        if r == N - 1 and c == N - 1:
            return cost

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = graph[nr][nc] + cost
                # 새로운 값이 더 작다면 더 작은 값으로 업데이트
                if new_cost < costs[nr][nc]:
                    # 업데이트
                    costs[nr][nc] = new_cost
                    # heap에 추가
                    heappush(pq, (new_cost, nr, nc))
    return costs[N - 1][N - 1]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph = []
    for _ in range(N):
        row = list(map(int, input()))
        graph.append(row)

    result = dijkstra(0, 0)
    print(f'#{test_case} {result}')