from heapq import heappush, heappop
def dijkstra(start_node):
    pq = [(0, start_node)] # (거리, 시작 노드)
    dists = [INF] * V
    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq)
        # dists[node]는 최솟값으로 계속 업데이트 되는 리스트
        # dist는 내가 지금 방문할 곳(조건이 안맞으면 안할 수도 있음)에서의 값(가중치)
        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue

            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))
    
    return dists[N]

# 최소 거리
T = int(input())
for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    V = N + 1
    INF = float('inf')    
    start_node = 0
    graph = [[] for _ in range(V)]
    for _ in range(E):
        start, end, distance = map(int, input().split())
        graph[start].append((distance, end))
    
    result = dijkstra(0)
    print(f'#{test_case} {result}')