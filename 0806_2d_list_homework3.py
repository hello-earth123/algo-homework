
for test_case in range(10):
    T = int(input())

    total = []
    arr = []
    total_cross = 0
    for _ in range(100):
        row = list(map(int, input().split()))
        arr.append(row)


    # 행 합 
    for row in arr:
        total.append(sum(row))


    # 열 합
    arr_transpose = list(zip(*arr))
    for col in arr_transpose:
        total.append(sum(col))


    # 대각선 합 1
    for i in range(100):
        total_cross += arr[i][i]
    total.append(total_cross)
    

    
    total_cross = 0
    # 대각선 합 2
    for r in range(100):
        for c in range(100):
            if r+c == 99:
                total_cross += arr[r][c]
    total.append(total_cross)

    print(f'#{T} {max(total)}')