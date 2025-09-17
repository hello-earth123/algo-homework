# G는 길
# T는 벽
# X는 차 위치
# Y는 목적지
# A: 앞으로 이동 L: 왼쪽으로 회전 R: 오른쪽으로 회전
# 나무가 있거나 범위를 벗어나면 제자리에 존재
from collections import deque
def goal():
    for r in range(N):
        for c in range(N):
            # 시작 위치
            if road[r][c] == 'X':
                start_row, start_col = r, c
            # 목적지
            elif road[r][c] == 'Y':
                goal_row, goal_col  = r, c
                
    queue = deque([(start_row, start_col)])
    # delta (상에서 시작 -> 시계방향) 
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    d = 0   # 방향
    result = 0
    
    while queue:
        for dir in command:
            # if queue:
            if dir == 'A':
                r, c = queue.popleft()
                # 이동
                nr, nc = r + dr[d % 4], c + dc[d % 4]
                if 0 <= nr < N and 0 <= nc < N and road[nr][nc] != 'T':
                    # 이동 가능하면 전진
                    queue.append((nr, nc))
                else:
                    # 아니면 다시 넣어놓기
                    queue.append((r, c))
            elif dir == 'L':
                # 방향 회전
                d -= 1
            elif dir == 'R':
                # 방향 회전
                d += 1
        # 현재 목적지 위치 한다면 result = 1
        goal_r, goal_c = queue.popleft()
        if goal_r == goal_row and goal_c == goal_col:
            result = 1

    return result

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    road = []
    for _ in range(N):
        row = input()
        road.append(row)

    Q = int(input())
    r = []
    for _ in range(Q):
        command_number, command = input().split()
        command_number = int(command_number)
        r.append(goal())

    print(f'#{test_case}', end = ' ')
    print(*r)