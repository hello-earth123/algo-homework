# 최악의 케이스는 A: 3000 B: 3000 C: 3인 경우
    # -> 2999x2998만큼의 연산이 발생 (약 900만 번)
    # -> 비효율적
# 한 번에 보낼 수 있는 방법은 없나?
# B = C -1 로 만들고 A = B - 1 로 만들어서 훅 건너 뛴다
    # 반복문 필요 없음

T = int(input())

for test_case in range(1, T+1):
    boxes = list(map(int, input().split()))
    # 만약 마지막 박스에 사탕이 1개밖에 없으면 만들 수 없음
    if boxes[2] == 1 or boxes[2] == 2 or boxes[1] == 1:
        is_increasing = False
    else:
        is_increasing = True

    eat = 0
    if is_increasing:
        while not (boxes[0] < boxes[1] < boxes[2]):
            while boxes[0] >= boxes[1]:
                boxes[0] -= 1
                eat += 1
            while boxes[1] >= boxes[2]:
                boxes[1] -= 1 
                eat += 1
    else:
        eat = -1

    print(f'#{test_case} {eat}')

# import sys
# sys.stdin = open("input.txt")

# T = int(input())

# for tc in range(1, T + 1):
#     # 3개 정도는 따로 받자!
#     A, B, C = map(int, input().split())

#     # 불가능한 케이스를 먼저 지우자
#     if A < 1 or B < 2 or C < 3:
#         print(f'#{tc} -1')
#         continue

#     eat_count = 0
#     # B 상자 = C 상자 - 1 (B가 C보다 크거나 같을 때만)
#     if B >= C:
# 	    eat_count += B - (C - 1) # 핵심 keypoint
# 	    B =  C - 1               # 핵심 keypoint
         
#     # A 상자 = B 상자 - 1 (A가 B보다 크거나 같을 때만)
#     if A >= B:
# 	    eat_count += A - (B - 1) # 핵심 keypoint
# 	    A = (B - 1)

#     print(f'#{tc} {eat_count}')