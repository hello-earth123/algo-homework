# 이동하려는 방이 현재 방 보다 1 커야함
from collections import deque
def move(row, col):
    cnt = 1
    queue = deque([(row, col)])
    # delta
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == board[r][c] + 1:
                    cnt += 1
                    queue.append((nr, nc))
    return cnt

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)

    result_count = 1
    for r in range(N):
        for c in range(N):
            count = move(r, c)
            if result_count > count:
                result_count = count
                result_num = board[r][c]
            
            elif count == result_count and board[r][c] < result_num:
                result_num = board[r][c] 

    print(f'#{test_case} {result_num} {result_count}')