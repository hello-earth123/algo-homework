# 높이가 B인 선반
# N명의 점원
# 점원의 키 H
# 탑의 높이는 B 이상
# B 이상인 것 중에서 가장 낮은 값
def tower(height, idx):  # 파라미터: 탑의 높이, 사람 수
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
    result = float('inf')   # 정답이 항상 보장된 경우는 이렇게 해도됨
                            # 보장되지 않는다면 최대 값으로 넣어야함

    tower(0, 0)
    print(f'#{test_case} {result}')

# N 명에서 특정 몇 명을 고르는건데
    # 조합 문제인가?
        # 근데 몇 명을 뽑는지 모르겠는데?
            # -> 부분 집합을 구하는 문제다.