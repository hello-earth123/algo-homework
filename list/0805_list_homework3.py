# 가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업 = dump

# 가로 길이는 항상 100
# 1 <= 상자의 높이(height) <= 100
# 1 <= dump 횟수(dump) <= 1000

T = 10

for test_case in range(1, T+1):
    dump = int(input())

    height = list(map(int, input().split()))

    # 제일 높은 위치와 제일 낮은 위치를 각각 +1 / -1한다.
    # max와 min이 바뀐다.
    # 위 for문을 반복한다.

    for _ in range(dump):
        
        height.sort()
        height[-1] -= 1
        height[0] += 1
        
    height.sort()
    result = height[-1] - height[0]

    print(f'#{test_case} {result}')