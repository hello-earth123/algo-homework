# 최적 경로
# 모두 방문, 총 이동거리가 가장 짧은 경로
import math
def recur(x, y, dist, cnt):
    global result
    if cnt == N:
        dist += (abs(home[0] - x) + abs(home[1] - y))
        if result > dist:
            result = dist
        return
    
    # pruning
    if dist >= result:
        return
    
    for nx, ny in location:
        if not visited[nx][ny]:
            visited[nx][ny] = True
            recur(nx, ny, dist + (abs((nx - x)) + abs((ny - y))), cnt + 1)
            # 백트래킹
            visited[nx][ny] = False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    company = (arr[0], arr[1])
    home = (arr[2], arr[3])

    location = []
    for i in range(4, len(arr) - 1, 2):
        loc = (arr[i], arr[i + 1])
        location.append(loc)
    # print(location)

    visited = [[False] * 101 for _ in range(101)]
    result = float('inf')
    recur(company[0], company[1], 0, 0)
    print(f'#{test_case} {result}')