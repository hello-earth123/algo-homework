# 제한 없음
# 만들 수 있는 숫자의 갯수
from collections import deque
def dfs(r, c, numbers):
    global num
    if len(numbers) == 7:
        if numbers not in num:
            num.append(numbers)
        return 
    
    # delta
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, numbers + board[nr][nc])


T = int(input())

for test_case in range(1, T + 1):
    board = []
    for _ in range(4):
        row = list(input().split())
        board.append(row)
    # print(board)

    num = []
    for r in range(4):
        for c in range(4):
            dfs(r, c, '' + board[r][c])
    # print(num)
    print(f'#{test_case} {len(num)}')