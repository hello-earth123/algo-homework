# 1은 가위, 2는 바위, 3은 보
# 같은 카드인 경우 번호가 작은 쪽을 승자로 한다.
# 처음 선택한 카드는 바꾸지 않는다.
# 1은 3한테 이기고
# 2는 1한테 이기고
# 3은 2한테 이긴다.

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    rps_num = list(map(int, input().split()))

    group1 = []
    group2 = []
    for idx in range(N):
        if id(group1) == id(group2):
            pass