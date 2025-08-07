for test_case in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착 지점의 열(col) 위치 찾기 (맨 아래 2 찿기)
    r = 99
    c = ladder[99].index(2)


    # 델타 좌우
    dr = [0, 0, -1]  # 좌, 우, 상
    dc = [-1, 1, 0]

    while r > 0:

        # 왼쪽으로 갈 수 있을 때
        if c > 0 and ladder[r][c-1] == 1:
            while c > 0 and ladder[r][c-1] == 1:
                c -= 1
            # 왼쪽으로 못 가면 위로 한 칸
            r -= 1

        # 오른쪽으로 갈 수 있을 때
        elif c < 99 and ladder[r][c+1] == 1:
            while c < 99 and ladder[r][c+1] == 1:
                c += 1

            # 오른쪽으로 못 가면 위로 한 칸
            r -= 1  

        # 양쪽 다 못 가면 위로
        else:
            r -= 1

    print(f'#{T} {c}')
