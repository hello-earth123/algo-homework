def recur(total, idx):
    global cnt
    if total == K:
        cnt += 1
        # print(*path)
        return
    
    if idx == N:
        return
    
    # 넣거나
    recur(total + numbers[idx], idx + 1)
    # 안넣거나
    recur(total, idx + 1)

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    cnt = 0
    recur(0, 0)
    print(f'#{test_case} {cnt}')