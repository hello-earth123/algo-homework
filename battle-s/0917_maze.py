from collections import deque
def bfs(start_r, start_c, goal_r, goal_c):
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    # delta
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    is_arrived = 0
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < 16 and 0 <= nc < 16 and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc))
        if visited[goal_r][goal_c]:
            is_arrived = 1
            break
    return is_arrived
    
for _ in range(10):
    test_case = int(input())
    maze = []
    for _ in range(16):
        row = input().strip()
        maze.append(row)
    visited = [[False] * 16 for _ in range(16)]
    
    for i in range(16):
        for j in range(16):
            # 출발점
            if maze[i][j] == '2':
                start_row, start_col = i, j
            # 도착점
            elif maze[i][j] == '3':
                goal_row, goal_col = i, j
            # 벽
            elif maze[i][j] == '1':
                visited[i][j] = True    
    result = bfs(start_row, start_col, goal_row, goal_col)
    print(f'#{test_case} {result}')