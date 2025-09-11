# 높이가 B인 선반
# N명의 점원
# 점원의 키 H
# 탑의 높이는 B 이상
# B 이상인 것 중에서 가장 낮은 값
def tower(height, idx):  # 파라미터: 탑의 높이
    global result
    if height >= B:
        if result > (height - B):
            result = (height - B)
        return

    if idx == N:
        return
    
    # pruning
    if height - B > result:
        return
    
    # 선택 할지
    tower(height + heights[idx], idx + 1)
    # 선택 안할지
    tower(height, idx + 1)

T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    visited = [False] * N
    result = float('inf')

    tower(0, 0)
    print(f'#{test_case} {result}')