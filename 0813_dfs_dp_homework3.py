# A에서B로 가는 길이 있는가?
# 거슬러서 돌아갈 수 없다. (일방 통행)
# A = 0, B = 99로 고정
# 모든 길은 순서쌍으로 주어진다.
# 정점은 98개를 넘지 않는다. (출발점0과 도착점99 제외)
# 갈림길은 하나 아니면 두 개밖에 없다.

for test_case in range(1, 11):
    T, line = map(int, input().split())

    # 짝수번째가 시작점, 홀수번째가 끝점 ()
    node = list(map(int, input().split()))


    # 그래프 그리기
    graph = [[] for _ in range(100)]
    for idx in range(len(node)):
        if idx % 2 == 0:
            graph[node[idx]].append(node[idx+1]) # node의 홀수 번째를 

    # print(graph)

    # 정렬
    for lst in graph:
        lst.sort()

    visited = [False] * (100)
    stack = [0]

    # 탐색 시작
    result = 0
    while stack:
        visit = stack.pop()
        visited[visit] = True

        for next_visit in reversed(graph[visit]):
            if not visited[next_visit]:
                stack.append(next_visit)

    # 99에 도달했다면 1 아니면 0
    if visited[99] == True:
        result = 1

    print(f'#{test_case} {result}')