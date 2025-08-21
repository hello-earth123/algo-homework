from collections import deque
T = int(input())

# bfs 함수
def bfs(start): 
    # 시작지점 정하기
    queue = deque([start])
    # 첫 노드 방문 처리
    visited_bfs[start] = True
    # 다음부터 끝날 때 까지 재귀
    while queue:
        node = queue.popleft()
        for next_visit in graph[node]:
            # 방문 처리 여부
            if not visited_bfs[next_visit]:
                # 방문처리 하고
                visited_bfs[next_visit] = True

                # 거리 계산 먼저 하고 나서 다음에 갈 노드 업데이트
                # 방금 내가 pop한 곳부터 연결된 인접 노드(직전에 방문 처리 한 노드)까지
                # 거리 계산
                road[next_visit] = road[node] + 1
                queue.append(next_visit)


for test_case in range(1, T+1):
    # V는 노드의 갯수, E는 간선의 갯수(몇 번을 이어주냐)
    V, E = map(int, input().split())

    # 간선 거리 표현
    road = [0] * (V+1)
    visited_bfs = [False] * (V+1)

    # 무방향 그래프 그리기
    graph = [[] for _ in range(V+1)] 
    for _ in range(E):
        start, end = map(int, input().split())

        graph[start].append(end)
        graph[end].append(start)
    # print(graph)

    # 시작 노드와 도착 노드
    S, G = map(int, input().split())

    # 함수 호출(탐색 시작)
    bfs(S)

    if visited_bfs[G] == False:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} {road[G]}')