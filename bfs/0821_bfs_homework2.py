from collections import deque
T = int(input())

def bfs(start_row, start_col):
    # 시작할 곳 튜플의 형태로 append
    queue = deque([(start_row, start_col)])
    visited_bfs[start_row][start_col] = True

    # 델타(우, 하, 좌, 상)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited_bfs[nx][ny] == False :
                # 거리 계산
                road[nx][ny] = road[x][y] + 1
                # 방문 표시
                visited_bfs[nx][ny] = True
                # 큐에 push
                queue.append((nx, ny))
        

for test_case in range(1, T+1):
    N = int(input())

    # 미로 방문 여부 리스트 생성
    visited_bfs = [([False] * N) for _ in range(N)]

    # 거리 구하기
    road = [([0] * N) for _ in range(N)]

    # 미로 만들기
    maze = []
    for _ in range(N):
        row = list(map(int, input()))
        maze.append(row)
    # print(maze)
    
    
    # 시작 지점, 끝 지점 찾기 / 벽인곳 다 True로 만들기
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                start_r, start_c = r, c

            elif maze[r][c] == 1:
                visited_bfs[r][c] = True
    # print(road)
    # print(visited_bfs)
    
    # 함수 호출(탐색 시작)
    bfs(start_r, start_c)
    # print(road)
    # print(visited_bfs)
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 3 and visited_bfs[r][c] == True:
                print(f'#{test_case} {road[r][c]-1}')
            elif maze[r][c] == 3 and visited_bfs[r][c] == False:
                print(f'#{test_case} 0')