# 모두 연결
# 신장 트리 
# 최소 신장 트리를 구한다. (E * (L ** 2))


# ----------------------------kruskal
from heapq import heappush, heappop
def find_set(x):
    if x == parents[x]:
        return parents[x]
    
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    # 좌표값 coord
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # 환경 부담 세율
    E = float(input())

    graph = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            cost = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) * E
            graph.append((cost, i, j))

    graph.sort()
    parents = [i for i in range(N)]
    cnt = 0
    result = 0

    for cost, u, v in graph:
        if find_set(u) != find_set(v):
            union(u, v)
            cnt += 1
            result += cost

            if cnt == N - 1:
                break

    print(f'#{test_case} {round(result)}')
    
# ---------------------------------prim
from heapq import heappush, heappop
def prim(start_node):
    # 비용, 정점
    pq = [(0, 0)]
    # 방문 여부
    visited = [0] * N
    min_weight = 0
    # MST에 포함된 정점 수
    cnt = 0

    while pq:
        cost, node = heappop(pq)
        if visited[node]:
            continue
        
        visited[node] = 1
        min_weight += cost
        cnt += 1

        for next_node in range(N):
            if not visited[next_node]:
                dist = ((x[node] - x[next_node])**2 + (y[node] - y[next_node])**2) * E
                heappush(pq, (dist, next_node))

    return min_weight

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    # 좌표값 coord
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # 환경 부담 세율
    E = float(input())

    result = prim(0)

    print(f'#{test_case} {round(result)}')