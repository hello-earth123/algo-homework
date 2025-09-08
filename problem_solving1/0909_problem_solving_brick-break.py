T = int(input())

for test_case in range(1, T+1):
    N, W, H = map(int, input().split())

    bricks = []
    for _ in range(H):
        row = list(map(int, input().split()))
        bricks.append(row)
    