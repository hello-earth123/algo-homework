# 사각형 모양을 그리며 다시 복귀
# 같은 숫자의 디저트 카페면 안감
# 디저트를 가장 많이 먹는 경우의 수
# 디저트 못 먹으면 -1 출력

# delta
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]
def cafe(r, c, dessert, direction):
    global result 
    for d in range(direction, direction + 2):
        nd = d % 4
        nr, nc = r + dr[nd], c + dc[nd]

        if 0 <= nr < N and 0 <= nc < N:
        # 종료 조건 (돌아와야함)
            if nr == start_r and nc == start_c and dessert >= 4:
                result = max(result, dessert)
                return
            
            if not visited_dessert[arr[nr][nc]]:
                visited_dessert[arr[nr][nc]] = True

                cafe(nr, nc, dessert + 1, nd)
            
                # 백트래킹
                visited_dessert[arr[nr][nc]] = False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    visited = [[False] * N for _ in range(N)]
    visited_dessert = [False] * 101

    result = -1
    for i in range(N):
        for j in range(N):
            start_r, start_c = i, j
            visited_dessert[arr[i][j]] = True
            cafe(start_r, start_c, 1, 0)
            visited_dessert[arr[i][j]] = False

    print(f'#{test_case} {result}')