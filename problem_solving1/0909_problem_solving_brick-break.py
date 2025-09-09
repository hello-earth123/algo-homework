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


# # 1. 최소 벽돌
# #  - 현재 벽돌이 다 깨지면 더 이상 할 필요 없다 -> 현재 벽돌 수를 관리

# # 2. N 번의 구슬을 굴려야 한다.
# # - 모든 케이스를 보아야 한다. (12^4, 약 25만 번)
# #   - 백트래킹
# # - 한 번 쏘았을 때 벽돌들이 연쇄로 깨진다.
# #   - 현재 기준으로 퍼져나가면서 탐색(BFS) -> 25만 번의 BFS??
# #   - 빈 칸 매꾸기 (중력 작용)
# from collections import deque
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]

# def shoot(cnt, remains, now_arr): # 남은 구슬 수와 남은 벽돌 수를 파라미터로
#     global min_blocks
#     # 종료 조건: N개의 구슬을 모두 발사 or 남은 벽돌이 0이면
#     if cnt == N or remains == 0:
#         min_blocks = min(min_blocks, remains)
#         return
    
#     # 모든 열에 한 줄 씩 떨구자
#     for col in range(W):
#         # 기존 벽돌들의 상태를 저장
#         # 방법1. 원본을 복사해두고, 다시 되돌리는 방법
#         # 1. col 위치에 떨구기 전 상태를 복사 (얕은 복사 주의)
#         # 2. 원본 리스트의 col 위치에 떨구고
#         # 3. cnt + 1 번 재귀 상태로 이동
#         # 4. 떨구기 전 상태로 복구

#         # 방법2. 복구 시간이 없는 방식
#         # 1. col 위치에 떨구기 전 상태를 복사
#         # 2. 복사한 리스트의 col 위치에 떨군다.
#         # 3. cnt + 1 번 상태로 이동할 때, copy_arr을 함께 전달
#         copy_arr = [row[:] for row in now_arr]
    
#         row = -1
#         # 가장 위 벽돌을 검색
#         for r in range(H):
#             if copy_arr[r][col]: # 벽돌이 있으면
#                 row = r
#                 break

#         if row == -1: # 벽돌이 없는 열은 pass
#             continue

#         # 해당 row, col의 숫자부터 시작해서 BFS
#         # 행, 열, 숫자를 모두 담아야 한다.
#         q = deque([(row, col, copy_arr[row][col])])
#         now_remains = remains - 1
#         copy_arr[row][col] = 0 # 구슬이 처음 만나는 벽돌 자기

#         # 주변 벽돌들을 순차적으로 파괴
#         while q:
#             r, c, p = q.popleft()
#             # 상하좌우의 p 칸을 모두 제거
#             for k in range(1, p):
#                 for i in range(4):
#                     nr = r + dy[i] * k
#                     nc = c + dx[i] * k

#                     # 범위 밖이면 pass
#                     if nr < 0 or nr >= H or nc < 0 or nc >= W:
#                         continue
#                     # 벽돌이 없으면 pass
#                     if copy_arr[nr][nc] == 0:
#                         continue

#                     q.append((nr, nc, copy_arr[nr][nc])) # 다음 벽돌 추가
#                     copy_arr[nr][nc] = 0                 # 벽돌 깨짐
#                     now_remains -= 1                     # 숫자 감소
#         # 빈칸을 메우기
#         ###########
        
#         ###########
#         shoot(cnt + 1, now_remains, copy_arr)

# T = int(input())

# for tc in range(1, T + 1):
#     N, W, H = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(H)]
#     min_blocks = float('inf') # 최소 벽돌 수
#     blocks = 0 
#     # 남은 벽돌 수
#     for i in range(H):
#         for j in range(W):
#             if arr[i][j]:
#                 blocks += 1

#     shoot(0, blocks, arr)
#     print(f'#{tc} { min_blocks}')