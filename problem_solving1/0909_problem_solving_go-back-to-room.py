T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    corridor = [0] * 201  # 복도는 최대 200칸 (방 400개니까 (400+1)//2 = 200)

    for _ in range(N):
        # a 방에서 b방까지
        a, b = map(int, input().split())
        # 어느 복도 사용?
        a = (a + 1) // 2 # a 복도부터 
        b = (b + 1) // 2 # b 복도까지
        # 경로 통일
        if a > b:
            a, b = b, a
        # 누적합 (특정 복도를 몇 명이나 사용하는지)
        for i in range(a, b + 1):
            corridor[i] += 1

    print(f"#{test_case} {max(corridor)}")
