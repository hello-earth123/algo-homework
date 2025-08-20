def find_min_sum(idx, current_sum):
    global min_sum

    # 가지치기
    # 현재까지의 합이 이미 기록된 최소 합 보다 크거나 같으면 컷
    if current_sum >= min_sum:
        return

    # 기저조건
    # 모든 행에 대한 선택을 완료했을 때 함수 종료
    if idx == N:
        if current_sum < min_sum:
            min_sum = current_sum
        return
    
    # 유도조건
    # 현재 행에서 사용할 열을 선택함.
    # 0번 열부터 N-1번 열 까지 모두 시도
    for i in range(N): 
        if not visited[i]:
            # 선택한 열은 사용한다고 표시하기
            visited[i] = True
            # 다음 행으로 이동, 현재 위치의 값을 합계에 더함 (idx는 세로 i는 가로를 순회한다.)
            find_min_sum(idx+1, current_sum + arr[idx][i])
            # 백트래킹
            visited[i] = False

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    min_sum = float('inf')

    # 열 사용 여부 체크할 배열
    visited = [False] * N

    find_min_sum(0, 0)

    print(f'#{test_case} {min_sum}')