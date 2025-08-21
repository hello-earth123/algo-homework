# V는 노드의 갯수, E는 간선의 갯수(몇 번을 이어주냐)
V, E = map(int, input().split())

# 무방향 그래프 그리기
graph = [[] for _ in range(V+1)] 
for _ in range(E):
    S, G = map(int, input().split())

    graph[S].append(G)
    graph[G].append(S)

    # print(graph)
    
##############################################################################
############################### 그래프 그리기###################################

# 여기서 V는 노드의 갯수
visited_dfs = [False] * (V+1)

def dfs(node):
    # 현재 노드 방문 처리 (현재 노드는 node이다)
    visited_dfs[node] = True

    # '인접한' 다음 노드에서
    for next_visit in graph[node]:
        # 만약에 방문하지 않았다면
        # 재귀 호출(while문 stack에 append()하는 방식과 같음)
        if not visited_dfs[next_visit]:
            dfs(next_visit)
'''
dfs()안에 들어갈 파라미터는 탐색의 시작 지점이다.
재귀함수 자체가 스택의 원리처럼 LIFO방식이기 때문에 굳이 stack에 쌓아서 만들 필요가 없다.
내가 방문할 곳(인접한 노드 중에 아직 방문하지 않은 곳)을 미리 stack에 저장하고 방문했으면 pop하는 형식
'''
from collections import deque
visited_bfs = [False] * (V+1)
def bfs(start_node):
    
    # 먼저 큐를 만듦과 동시에 시작 노드 큐에 넣기
    queue = deque([start_node])
    # 시작 노드 방문처리
    visited_bfs[start_node] = True

    # 큐가 빌 때까지 반복한다.
    while queue:
        # 방문했으면 꺼내야지
        node = queue.popleft()

        # 그 꺼낸(방문한) 노드의 인접노드들을 봤을 때
        for next_visit in graph[node]:
            # 아직 방문하지 않았다면
            if not visited_bfs[next_visit]:
                # 방문 처리를 해주고
                visited_bfs[next_visit] = True
                queue.append(next_visit)
'''
bfs()안에 들어갈 파라미터는 탐색의 시작 지점이다.
FIFO 형식이므로 재귀함수의 형태를 만들 수 없다.
반드시 함수 호출 시에 덱을 만들고 그 안에서 처리한다.
큐는 내가 방문할 곳(인접한 노드 중에 아직 방문하지 않은 곳)을 미리 큐에 저장해놓고 그 순서대로 방문
대기줄과 같다.
'''

'''
이것이 핵심입니다. 만약 visited = True 처리를 큐에서 노드를 꺼낼 때(pop) 한다고 상상해 보세요. 다음과 같은 심각한 문제가 발생합니다.

1번 노드를 처리하면서 이웃인 2번, 3번을 봅니다.

둘 다 방문 전이므로 큐에 [2, 3]을 넣습니다.

다음으로 2번 노드를 처리하면서 이웃인 1번, 3번, 4번을 봅니다.

이때, 3번은 아직 visited가 False입니다! (큐에 들어있기만 할 뿐, 아직 처리(pop)된 적이 없으므로)

따라서 2번 노드는 3번을 또 큐에 넣게 됩니다.

결과: 큐는 [3, 3, 4] 와 같이 중복된 값으로 가득 차게 되고, 메모리와 시간 낭비가 발생합니다.

따라서 BFS에서는 큐에 노드를 넣는 시점에 즉시 "방문 예약"의 의미로 visited = True 처리를 해야만 동일한 노드가 큐에 여러 번 들어가는 비효율을 완벽히 막을 수 있습니다.
'''


visited_dfs = [False] * (V+1)
def dfs(node):
    visited_dfs[node] = True

    for next_visit in graph[node]:
        if not visited_dfs[next_visit]:
            dfs(next_visit)


visited_bfs = [False] * (V+1)
def bfs(start_node):
    queue = deque([start_node])
    if not visited_bfs[start_node]:
        visited_bfs[start_node] = True

        while queue:
            node = queue.popleft()
            for next_visit in graph[node]:
                if not visited_bfs[next_visit]:
                    visited_bfs[next_visit] = True
                    queue.append(next_visit)
                    