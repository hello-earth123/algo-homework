T = int(input())

for test_case in range(1, T+1):
    N = int(input())


    # 미로 생성
    # 0은 통로, 1은 벽, 2는 출발, 3은 도착
    maze = []
    for _ in range(N):
        row = list(map(int, input()))
        maze.append(row)

    # 델타 (우, 하, 좌, 상)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]


    # 방문 여부 check -> 방문 한 곳이면(True) 재방문 방지
    visited_dfs = []
    for _ in range(N):
        width = [False] * N
        visited_dfs.append(width)

    # 통로 다 막기, 시작지점 찾기
    found = False
    for r in range(N):
        for c in range(N):
            # 1이면 통로
            if maze[r][c] == 1:
                visited_dfs[r][c] = True
            # 2면 시작지점
            if maze[r][c] == 2:
                start_r, start_c = r, c
                found = True
                break
        if found:
            break
    
    # 탐색 시작
    stack = [(start_r, start_c)]
    escape = False
    while stack:
        visited_r, visited_c = stack.pop()
        visited_dfs[visited_r][visited_c] = True

        # 사방 탐색
        for i in range(4):
            v_r = visited_r + dx[i]
            v_c = visited_c + dy[i]
            # 3을 발견 했으면 result = 1하고 정지
            if (0 <= v_r < N) and (0 <= v_c < N) and (maze[v_r][v_c] == 3):
                result = 1
                escape = True
                break
            # 범위 내에 있는 통로고 아직 방문 안했다면 stack에 append
            elif (0 <= v_r < N) and (0 <= v_c < N) and (maze[v_r][v_c] == 0) and not visited_dfs[v_r][v_c]:
                stack.append((v_r, v_c))
        # 탈출
        if escape:
            break
        # 3 발견 못했으면 탈출 불가능
        else:
            result = 0
    
    print(f'#{test_case} {result}')


        