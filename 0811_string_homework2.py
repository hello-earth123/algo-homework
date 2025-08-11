for test_case in range(1, 11):
    length = int(input())


    # 글자판 만들기
    puzzle = []
    for _ in range(8):
        row = input()
        puzzle.append(row)

    count = 0
    # 가로 순회
    for r in range(8):
        for c in range(9-length):
            if all(puzzle[r][c+idx] == puzzle[r][c+(length-1)-idx] for idx in range(length//2)):
                count += 1

    # 세로 순회
    for c in range(8):
        for r in range(9-length):
            if all(puzzle[r+idx][c] == puzzle[r+(length-1)-idx][c] for idx in range(length//2)):
                count += 1

    # 출력
    print(f'#{test_case} {count}')