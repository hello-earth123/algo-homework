T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    # 전진할 때 채워지는 숫자
    number = 1

    # 달팽이 껍데기
    snail = []
    for _ in range(N):
        row = [0] * N
        snail.append(row)


    # 델타 (우,하,좌,상 순서)
    dx = [0, 1, 0, -1]    
    dy = [1, 0, -1, 0]
    idx = 0

    # 초기 위치 / 초기 번호
    r = 0
    c = 0
    snail[r][c] = number
    

    
    # 달팽이 출발
    while number < N * N:

        # 전진하는 방향 지정
        nr = r + dx[idx]
        nc = c + dy[idx]


        # 범위 내에 있고, 아직 안채운 칸이면 (아직 0이면) 채워야함
        if 0 <= nr < N and 0 <= nc < N and snail[nr][nc] == 0:
            number += 1
            snail[nr][nc] = number
            r, c = nr, nc

        # 만약 벗어나거나 이미 채운 칸을 만난다면 방향을 바꾼다. (우, 하, 좌, 상 순서로) 
        else:
            idx = (1+idx) % 4
    

    print(f'#{test_case}')
    for row in snail:
        print(*row)

