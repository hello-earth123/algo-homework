from collections import deque
def bfs(N, M):
    queue = deque([(N, 0)])
    visited = [False] * 1000001

    while queue:
        num, count = queue.popleft()

        if num == M:
            return count

        # visited 배열을 통해 가장 최소 연산 길이를 보장하도록 한다.
        for next_visit in (num + 1, num - 1, 2 * num, num - 10):
            if 0<= next_visit <= 1000000 and not visited[next_visit]:
                visited[next_visit] = True
                queue.append((next_visit, count + 1))

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    result = bfs(N, M)
    print(f'#{test_case} {result}')