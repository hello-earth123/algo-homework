# N개의 컨테이너
# M개의 트럭
# 트럭당 한 개의 컨테이너
# 적재량을 초과하면 안됨
# 컨테이너 무게, 적재 용량 
# 최대 M대의 트럭이 운행
# 이동한 화물의 총 중량이 최대가 되도록
# 화물의 전체 무게는?
# 컨테이너를 한 개도 옮길 수 없다면 0

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N: 컨테이너 수 M: 트럭 수
    # 각 컨테이너 무게
    weights = list(map(int, input().split()))
    # 트럭 최대 적재
    truck_max = list(map(int, input().split()))
    weights.sort(reverse=True)
    truck_max.sort(reverse=True)
    total = 0
    is_possible = False
    while truck_max and weights:
        if truck_max[0] >= weights[0]:
            is_possible = True
            truck_max.pop(0)
            weight = weights.pop(0)
            total += weight
        else:
            weights.pop(0)
            
    if not is_possible:
        total = 0

    print(f'#{test_case} {total}')


