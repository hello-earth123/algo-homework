T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    maze = []
    for _ in range(N):
        row = list(map(int, input().split()))
        maze.append(row)
    
    # 방문 처리
    visited = [False] * N
    # 결과값 -> 최소값
    result = float('inf')

    def battery(now, total, cnt): # now: 현재 위치 / total: 더해진 값을 저장 / cnt: 몇 번 돌았는지
        global result

        # 가지치기
        if total >= result: # 이미 total이 result를 넘어섰으면 의미가 없으므로 종료
            return
        
        # 종료
        if cnt == N - 1: # N-1번 돌았다면 종료
            result = min(result, total + maze[now][0])  # 마지막으로 출발한 곳에 도착해야하므로 maze[now][0]을 더해주면서 종료
            return
        
        # 다른 도시 방문
        for next_visit in range(1, N):
            if not visited[next_visit]:
                visited[next_visit] = True
                battery(next_visit, total + maze[now][next_visit], cnt + 1)
                # 백트래킹
                visited[next_visit] = False
        
    

    visited[0] = True
    battery(0, 0, 0)

    print(f'#{test_case} {result}')