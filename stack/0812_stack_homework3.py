T = int(input())

for test_case in range(1, T+1):
    
    # 삼각형 줄 수
    N = int(input())

    # 삼각형 만들기
    triangle = []
    for i in range(N):
        row = [1] * (i+1)
        triangle.append(row)

    for r in range(2, N):
        for c in range(1, r):
            triangle[r][c] = triangle[r-1][c-1] + triangle[r-1][c]

    
    
    # print(triangle)
    
    print(f'#{test_case}')
    for r in range(N):
        for c in range(r+1):
            print(f'{triangle[r][c]}', end = ' ')
        print()