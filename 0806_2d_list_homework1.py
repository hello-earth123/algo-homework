# from pprint import pprint

T = int(input())


# 왼쪽 위(r1, c1) / 오른쪽 아래 모서리(r2, c2) / 색상정보 순서(빨강 1, 파랑 2) 
for test_case in range(1, T+1):
    count = 0
    
    # 도화지 생성
    # 깊은 복사 해야됨
    # row를 생성할 때 무조건 안으로 집어 넣어서 row를 계속 생성해야됨
    paper = []
    for _ in range(10):
        row = [0] * 10
        paper.append(row)

    # pprint(paper)

    # 사각형 갯수
    N = int(input())   


    # 사각형 생성
    for _ in range(N):
        square = list(map(int, input().split()))

        
        # [2, 2, 4, 4, 1]
        # 사각형 색칠하기
        for r in range(square[0], square[2]+1):
            for c in range(square[1], square[3]+1):
                paper[r][c] += square[4]


    # pprint(paper)
    # 보라색이 된 칸 세기
    for r in range(10):
        for c in range(10):
            if paper[r][c] == 3:
                count += 1
    

    print(f'#{test_case} {count}')