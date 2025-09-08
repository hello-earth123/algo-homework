# 벽돌 부수기
def boom(r, c, board):
    p = board[r][c]
    board[r][c] = 0
    # p-1만큼 사방 탐색 후 조건을 만족하면 벽돌 깨서 0으로 만들기
    if p > 1:
        for i in range(4):
            for k in range(1, p):
                nr = r + dr[i] * k
                nc = c + dc[i] * k
                if 0 <= nr < H and 0 <= nc < W and board[nr][nc] != 0:
                    boom(nr, nc, board)
# 벽돌 떨구기             
def drop(board):
    for c in range(W):
        stack = []
        for r in range(H - 1, -1 , -1):
            if board[r][c] != 0:
                stack.append(board[r][c])
                board[r][c] = 0

        r = H - 1
        for val in stack:
            board[r][c] = val
            r -= 1
            
# 남은 벽돌 세기   
def count_bricks(board):
    count = 0
    for r in range(H):
        for c in range(W):
            if board[r][c] != 0:
                count += 1
    return count

# 시뮬레이션
def simulation(cnt, board):
    global result
    if cnt == N:
        result = min(result, count_bricks(board))
        return
    
    is_moved = False
    for c in range(W):
        # 현재 벽돌을 deepcopy해서 시뮬레이션
        new_board = deepcopy(board)
        # 위에서부터 가장 처음 만나는 벽돌 찾기
        for r in range(H):
            if new_board[r][c] != 0:
                boom(r, c, new_board)
                drop(new_board)
                simulation(cnt + 1, new_board)
                is_moved = True
                break
            
    if not is_moved:
        # 벽돌 없으면 넘어가기
        simulation(cnt + 1, board)

# 실행
from copy import deepcopy
T = int(input())
for test_case in range(1, T+1):
    N, W, H = map(int, input().split())

    bricks = []
    for _ in range(H):
        row = list(map(int, input().split()))
        bricks.append(row)
    
    # delta
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    result = float('inf')
    simulation(0, bricks)
    print(f'#{test_case} {result}')