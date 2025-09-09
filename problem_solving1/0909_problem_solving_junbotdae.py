# 교차만 가능
# s, e는 안겹침
# 세 개 이상의 전선이 하나의 점에서 안만남

# 교점을 형성하려면
    # 평행하지 않는다.
    # 시작 지점과 끝 지점의 크기 차이가 반드시 뒤바껴야 한다.

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 전선의 갯수
    wires = []
    for _ in range(N):
        y1, y2 = map(int, input().split())

        wires.append((y1, y2))
    cnt = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            # 교차 조건
            if (wires[i][0] < wires[j][0] and wires[i][1] > wires[j][1]) or (wires[i][0] > wires[j][0] and wires[i][1] < wires[j][1]):
                cnt += 1

    print(f'#{test_case} {cnt}')

# # 완전 탐색
# # 새로운 선이 들어올 때 마다
#     # 기존의 모든 전선들과 비교

# # 기존 전선 : 1개
# # 비교 1번

# # 기존 전선 : 2개
# # 비고 2번

# # 기존 전선 : 3 개
# # 비교 3번

# # 기존 전선 : N - 1개
# # 비교 N -1번

# # 등차 수열 공식 -> N * (N - 1) / 2

# import sys
# sys.stdin = open("input.txt", "r")

# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())

#     # N개의 새로운 선이 추가 (기존 선들과 비교)
#     wires = []       # 기존 선들을 저장할 리스트
#     answer_count = 0 # 교차점 수

#     for _ in range(N):
#         start, end = map(int, input().split())

#         # 기존 선들과 비교 (교차점 비교)
#         for prev_start, prev_end in wires:
#         # 1. 기존의 전선보다 시작점이 높고, 도착점이 낮음
#             if start > prev_start and end < prev_end:
#                 answer_count += 1
#         # 2. 기존의 전선보다 시작점이 낮고, 도착점이 높음
#             if start < prev_start and end > prev_end:
#                 answer_count += 1
#         # 목록에 추가
#         wires.append((start, end))
#     print(f'#{tc} { answer_count}')