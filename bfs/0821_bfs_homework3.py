from collections import deque
def bfs(start_row, start_col):
    # 큐 생성
    queue = deque([(start_row, start_col)])
    # 시작 지점 방문 처리
    visited_bfs[start_row][start_col] = True

    # 탐색 끝날 때 까지 반복
    while queue:
        x, y = queue.popleft()
        # 사방 탐색 (우 하 좌 상)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16 and visited_bfs[nx][ny] == False:
                visited_bfs[nx][ny] = True
                queue.append((nx, ny))

for test_case in range(1, 11):
    T = int(input())

    # 미로 만들기
    maze = []
    for _ in range(16):
        row = list(map(int, input()))
        maze.append(row)

    # 방문 처리 여부 만들기
    visited_bfs = [([False] * 16) for _ in range(16)]

    # 델타(우 하 좌 상)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0] 

    # 시작 지점 찾기 / 벽 막기
    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                start_r, start_c = r, c

            elif maze[r][c] == 1:
                visited_bfs[r][c] = True

    # 함수 호출(탐색 시작)
    bfs(start_r, start_c)

    # 결과 출력
    for r in range(16):
        for c in range(16):
            if maze[r][c] == 3 and visited_bfs[r][c] == True:
                print(f'#{test_case} 1')
            elif maze[r][c] == 3 and visited_bfs[r][c] == False:
                print(f'#{test_case} 0')