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
        