graph = [] # 그래프 그려주면 된다.

def bfs(s, V): # s는 시작점, V는 끝점
    # 초기화
    visited = [0] * (V + 1) # visited 생성
    q = [s]                 # 큐 생성

    visited[s] = 1          # 시작점 인큐
    # 반복
    while q:                # 탐색할 정점이 남아 있으면
        t = q.pop(0)        # 디큐
        print(t)            # visit(), 방문 정점 출력해보자(안해도됨)

        for w in graph[t]:  # w가 next_visit이고 t가 visited랑 같은것 여기서 visited는 visited_dfs(or visited_bfs)와 같은 행렬
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1 # 방문 표시를 할건데 그것을 거리가 멀어지는 것으로 표현

    
# 1에서 각 정점까지 최소 거리(간선 수)의 합은?
# visited의 모든 값에 1을 빼주고 더한다. (모든 visited의 합에서 간선 갯수를 뺀 값)