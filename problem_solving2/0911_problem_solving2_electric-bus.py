# 최소갯수
def bus(start):
    global cnt, result
    if start == N-1:
        if cnt < result:
            result = cnt
        return
    
    # pruning
    if cnt >= result:
        return
    
    for i in range(1, charge[start] + 1):
        cnt += 1
        # 재귀호출
        bus(start + i)
        # 백트래킹
        cnt -= 1

T = int(input())

for test_case in range(1, T + 1):
    charge = list(map(int, input().split()))
    N = charge.pop(0)
    charge = charge + [0]
    # print(charge)
    
    cnt = 0
    result = float('inf')
    bus(0)
    # 도착할 때의 교환은 포함하지 않음
    print(f'#{test_case} {result - 1}')