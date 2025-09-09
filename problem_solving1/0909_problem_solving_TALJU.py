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

# # 지도 - 이차원 배열 형태

# # 맨홀 뚜껑으로부터 출발
#     # 터널들을 이동
#     # 이동 방향 : 상하좌우
#         # 델타 배열
#     # 이동 못하는 경우가 존재
#         # 현재 내 위치에서 뚫려있는 곳만 이동 가능
#         # 다음 위치의 입구가 똟려있는 곳으로만 가능


# # 설계
# # 점점 퍼져나가는 그림 -> (미생물, 바이러스, 폭탄, 군집 ..)
# # BFS (시작점부터 주변으로 점점 퍼져나가면서 확인)
#     # Queue를 활용해서 먼저 확인하는 노드부터 먼저 확인하자
#         # 먼저 방문한 노드에서 갈 수 있는 노드들을 후보군(Queue)에 추가

# # BFS의 시간복잡도
#     # O(V + E)
#     # V: 정점의 갯수 / E: 간선의 갯수
# from collections import deque
# import sys
# sys.stdin = open("input.txt", "r")

# # 1. BFS로 접근
#     # 이동 방향: 상하좌우
#     # 이동이 불가능한 케이스
#         # [델타 배열 기본] 범위 밖으로 나가면 못감
#         # [방문 기록 기본] 이미 방문한 곳은 못감
#         # 0이면 못감
#         # [문제 조건]
#             # 현재 내 위치에서 뚫려있는 곳만 이동 가능
#             # 다음 위치의 입구가 똟려있는 곳으로만 가능
#             # -> 이런 케이스들은 델타배열과 동일한 순서 (상하좌우)
#                 # 이동 가능 여부를 기록해두면 좋다.

# # 2. 방문 기록을 해야한다. (visited)

# # 델타 배열

# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]

# # 터널들의 종류에 따라, 이동 가능 여부를 기록
# types = {
#     # 상하좌우 순서로 기록 (가능하면 1, 불가능하면 0)
#     1 : [1, 1, 1, 1],
#     2 : [1, 1, 0, 0],
#     3 : [0, 0, 1, 1],
#     4 : [1, 0, 0, 1],
#     5 : [0, 1, 0, 1],
#     6 : [0, 1, 1, 0],
#     7 : [1, 0, 1, 0],
# }

# def bfs(R, C):
#     q = deque([(R, C)])    # 후보군
#     visited[R][C] = 1 # 출발점 초기화
    
#     while q: # 후보군이 없을 때 까지 (더 이상 방문할 수 있는 곳이 없으면 종료)
#         now_y, now_x = q.pop(0)
#         dirs = types[graph[now_y][now_x]]

#         for dir in range(4): # 상하좌우 확인
#             # 출구가 없으면 continue (다음 방향 확인)
#             if dirs[dir] == 0:
#                 continue
                
#             # 다음 좌표
#             new_y = now_y + dy[dir]
#             new_x = now_x + dx[dir]

#             # 범위 밖이면 pass
#             if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
#                 continue
#             # 못가는 못이면 pass
#             if graph[new_y][new_x] == 0:
#                 continue
#             # 이미 방문 했으면 pass
#             if visited[new_y][new_x]:
#                 continue
#             # 다음 좌표 터널 뚫린 것을 확인
#             next_dirs = types[graph[new_y][new_x]]
            
#             # 상좌는 오른쪽 옆에 +1을 해주고, 하우는 왼쪽 옆에 -1을 해줘서 체크한다.
#             # 현재 상좌 -> next_dirs의 하우가 안뚫렸으면 못간다.
#             if dir % 2 == 0 and next_dirs[dir + 1] == 0:
#                 continue
#             # 현재 하우 -> next_dirs의 상좌가 안뚫렸으면 못간다.
#             if dir % 2 == 1 and next_dirs[dir - 1] == 0:
#                 continue 
            
#             # L 시간 이후는 볼 필요 없다.
#             if visited[now_y][now_x] + 1 > L:
#                 continue


#             # 시간을 +1 해주면서 기록
#             visited[new_y][new_x] = visited[now_y][now_x] + 1
#             q.append((new_y, new_x))

# T = int(input())

# for tc in range(1, T + 1):
#     N, M, R, C, L = map(int, input().split())
#     graph = [list(map(int, input().split())) for _ in range(N)]
#     # 특정 좌표까지 몇 시간이 걸렸는지 기록
#     visited = [[0] * M for _ in range(N)]

#     bfs(R, C)
#     cnt = 0
#     # L 시간 이하로 방문한 모든 곳을 count
#     for i in range(N):
#         for j in range(M):
#             if 0 < visited[i][j] <= L:
#                 cnt += 1

#     print(f'#{tc} {cnt}')