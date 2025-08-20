T = int(input())

for test_case in range(1, T+1):

    V, E = map(int, input().split())


    # 그래프 그리기
    graph = [[] for _ in range(V+1)] # 노드 갯수+1 개 만큼 그린다. (노드는 1번부터 시작하므로) (graph의 0번 리스트는 안 쓰는 리스트)
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)


    # S와G가 이어지면 1 아니면 0    
    S, G = map(int, input().split())

    visited = [False] * (V+1)
    stack = [S]
    result = 0
    while stack:
        visit = stack.pop()
        visited[visit] = True


        for next_visit in graph[visit]:
            if not visited[next_visit]:
                stack.append(next_visit)

        if visited[G] == True:
            result = 1

    print(f'#{test_case} {result}')