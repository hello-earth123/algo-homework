# 회문은 한개 존재하면 가로 혹은 세로로 있음
# N은 판 크기 / M은 회문 길이


T = int(input())

for test_case in range(1, T + 1):
    string_board = []
    N, M = map(int, input().split())
    result = ''
    found = False

    # 글자판 만들기
    for _ in range(N):
        row = list(map(str, input()))
        string_board.append(row)


    #가로순회
    for r in range(N):
        for c in range(N-M+1):  # N-M의 인덱스 까지만 검사
            if all(string_board[r][c+j] == string_board[r][c+(M-1)-j] for j in range(M // 2)):
                result = ''.join(string_board[r][c:c+M])
                found = True
                break
        if found:
            break


    #세로순회
    #세로 문자열을 순회할 때는 슬라이싱으로는 절대 하면 안된다
    #세로를 슬라이싱하면 리스트 덩어리 여러개가 되므로
    #for문을 통해 글자 하나하나 순회하면서 붙여줘야한다.
    if not found:
        for c in range(N):
            for r in range(N-M+1):  # N-M의 인덱스 까지만 검사
                if all(string_board[r+j][c] == string_board[r+(M-1)-j][c] for j in range(M // 2)):
                    result = ''.join(string_board[r+k][c] for k in range(M))
                    found = True
                    break
            if found:
                break

    print(f'#{test_case} {result}')