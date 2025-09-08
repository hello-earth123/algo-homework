# 시간당 1의 거리
# 가로 6, 세로 5
#    1      2    3     4    5     6    7
# 상하좌우, 상하, 좌우, 상우, 하우, 하좌, 상좌
from collections import deque
def catch(maze):
    global cnt
    queue = deque([(R, C, 1)])
    visited[R][C] = True
    cnt += 1
    # delta (우, 하, 좌, 상)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while queue:
        x, y, time = queue.popleft()
        if time == L:
            continue

        # 상하좌우  
        if maze[x][y] == 1:
            for i in range(4): 
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if i == 0:
                        if (maze[nx][ny] == 1 or maze[nx][ny] == 3 or maze[nx][ny] == 6 or maze[nx][ny] == 7):
                            queue.append((nx, ny, time + 1))
                            visited[nx][ny] = True
                            cnt += 1
                    elif i == 1:
                        if (maze[nx][ny] == 1 or maze[nx][ny] == 2 or maze[nx][ny] == 4 or maze[nx][ny] == 7):
                            queue.append((nx, ny, time + 1))
                            visited[nx][ny] = True
                            cnt += 1
                    elif i == 2:
                        if (maze[nx][ny] == 1 or maze[nx][ny] == 3 or maze[nx][ny] == 4 or maze[nx][ny] == 5):
                            queue.append((nx, ny, time + 1))
                            visited[nx][ny] = True
                            cnt += 1
                    elif i == 3:
                        if (maze[nx][ny] == 1 or maze[nx][ny] == 2 or maze[nx][ny] == 5 or maze[nx][ny] == 6):
                            queue.append((nx, ny, time + 1))
                            visited[nx][ny] = True
                            cnt += 1
        
        # 상하
        elif maze[x][y] == 2:
            for i in range(4):
                if i % 2 != 0:
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if i == 1:
                            if (maze[nx][ny] == 1 or maze[nx][ny] == 2 or maze[nx][ny] == 4 or maze[nx][ny] == 7):
                                queue.append((nx, ny, time + 1))
                                visited[nx][ny] = True
                                cnt += 1
                        elif i == 3:
                            if (maze[nx][ny] == 1 or maze[nx][ny] == 2 or maze[nx][ny] == 5 or maze[nx][ny] == 6):
                                queue.append((nx, ny, time + 1))
                                visited[nx][ny] = True
                                cnt += 1
        
        # 좌우
        elif maze[x][y] == 3:
            for i in range(4):
                if i % 2 == 0:
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if i == 0:
                            if (maze[nx][ny] == 1 or maze[nx][ny] == 3 or maze[nx][ny] == 6 or maze[nx][ny] == 7):
                                queue.append((nx, ny, time + 1))
                                visited[nx][ny] = True
                                cnt += 1
                        elif i == 2:
                            if (maze[nx][ny] == 1 or maze[nx][ny] == 3 or maze[nx][ny] == 4 or maze[nx][ny] == 5):
                                queue.append((nx, ny, time + 1))
                                visited[nx][ny] = True
                                cnt += 1
        
        # 상우
        elif maze[x][y] == 4:
            for i in [0, 3]:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if i == 0:
                        if (maze[nx][ny] == 1 or maze[nx][ny] == 3 or maze[nx][ny] == 6  or maze[nx][ny] == 7):
                            queue.append((nx, ny, time + 1))
                            visited[nx][ny] = True
                            cnt += 1
                    elif i == 3:
                        if (maze[nx][ny] == 1 or maze[nx][ny] == 2 or maze[nx][ny] == 5 or maze[nx][ny] == 6):
                            queue.append((nx, ny, time + 1))
                            visited[nx][ny] = True
                            cnt += 1
        
        # 하우
        elif maze[x][y] == 5:
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if i == 0:
                        if (maze[nx][ny] == 1 or maze[nx][ny] == 3 or maze[nx][ny] == 6 or maze[nx][ny] == 7):
                            queue.append((nx, ny, time + 1))
                            visited[nx][ny] = True
                            cnt += 1
                    elif i == 1:
                        if (maze[nx][ny] == 1 or maze[nx][ny] == 2 or maze[nx][ny] == 4 or maze[nx][ny] == 7):
                            queue.append((nx, ny, time + 1))
                            visited[nx][ny] = True
                            cnt += 1
        
        # 하좌
        elif maze[x][y] == 6:
            for i in range(1, 3):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if i == 1:
                        if (maze[nx][ny] == 1 or maze[nx][ny] == 2 or maze[nx][ny] == 4 or maze[nx][ny] == 7):
                            queue.append((nx, ny, time + 1))
                            visited[nx][ny] = True
                            cnt += 1
                    elif i == 2:
                        if (maze[nx][ny] == 1 or maze[nx][ny] == 3 or maze[nx][ny] == 4 or maze[nx][ny] == 5):
                            queue.append((nx, ny, time + 1))
                            visited[nx][ny] = True
                            cnt += 1
        
        # 상좌
        elif maze[x][y] == 7:
            for i in range(2, 4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if i == 2:
                        if (maze[nx][ny] == 1 or maze[nx][ny] == 3 or maze[nx][ny] == 4 or maze[nx][ny] == 5):
                            queue.append((nx, ny, time + 1))
                            visited[nx][ny] = True
                            cnt += 1
                    elif i == 3:
                        if (maze[nx][ny] == 1 or maze[nx][ny] == 2 or maze[nx][ny] == 5 or maze[nx][ny] == 6):
                            queue.append((nx, ny, time + 1))
                            visited[nx][ny] = True
                            cnt += 1
            
        

T = int(input())
for test_case in range(1, T+1):
    # 세로, 가로, 맨홀뚜껑 r,c값, 시간
    N, M, R, C, L = map(int, input().split())
    # start = maze[R][C]
    visited = [[False] * M for _ in range(N)]

    maze = []
    for _ in range(N):
        row = list(map(int, input().split()))
        maze.append(row)

    cnt = 0
    catch(maze)
    print(f'#{test_case} {cnt}')