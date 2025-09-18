import heapq

def dijkstra(start_r, start_c):
    # (remote_count, r, c, cut_count, direction)
    heap = []
    heapq.heappush(heap, (0, start_r, start_c, 0, 0))
    visited[0][start_r][start_c][0] = True
    # delta
    dr = [-1, 0, 1, 0]  # 상, 우, 하, 좌
    dc = [0, 1, 0, -1]
    
    while heap:
        remote_count, r, c, cut_count, dir_prev = heapq.heappop(heap)
        
        # 목표 도착
        if (r, c) == (goal_row, goal_col):
            return remote_count
        
        # 1. 방향 전환 (좌회전, 우회전)
        nd_l = (dir_prev - 1) % 4
        nd_r = (dir_prev + 1) % 4
        if not visited[cut_count][r][c][nd_l]:
            visited[cut_count][r][c][nd_l] = True
            heapq.heappush(heap, (remote_count + 1, r, c, cut_count, nd_l))
        if not visited[cut_count][r][c][nd_r]:
            visited[cut_count][r][c][nd_r] = True
            heapq.heappush(heap, (remote_count + 1, r, c, cut_count, nd_r))

        # 2. 전진 (바라보는 방향으로)
        nr, nc = r + dr[dir_prev], c + dc[dir_prev]
        if 0 <= nr < N and 0 <= nc < N:             
            # 빈 칸 이동
            if road[nr][nc] == 'G' or road[nr][nc] == 'Y':
                if not visited[cut_count][nr][nc][dir_prev]:
                    visited[cut_count][nr][nc][dir_prev] = True
                    heapq.heappush(heap, (remote_count + 1, nr, nc, cut_count, dir_prev))
            # 나무 자르고 이동
            elif road[nr][nc] == 'T' and cut_count < K:
                if not visited[cut_count + 1][nr][nc][dir_prev]:
                    visited[cut_count + 1][nr][nc][dir_prev] = True
                    heapq.heappush(heap, (remote_count + 1, nr, nc, cut_count + 1, dir_prev))

    return -1  # 도착 불가

# 입력 처리
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    road = [input().strip() for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            if road[r][c] == 'X':
                start_row, start_col = r, c
            elif road[r][c] == 'Y':
                goal_row, goal_col = r, c
    
    # [자른 횟수][r 위치][c 위치][방향]
    visited = [[[[False] * 4 for _ in range(N)] for _ in range(N)] for _ in range(K + 1)]
    
    result = dijkstra(start_row, start_col)
    print(f"#{test_case} {result}")
