from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr = deque(list(map(int, input().split())))
    for _ in range(M):
        # rotate(1)은 제일 뒤에 있는게 앞으로 오게끔 회전 (시계 방향)
        # rotate(2)은 제일 앞에 있는게 제일 뒤고 가게끔 회전 (반시계 방향)
        arr.rotate(-1)

    print(f'#{test_case} {arr[0]}')