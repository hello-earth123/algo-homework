def probability(row, prob):
    global result
    if row == N:
        result = max(result, prob)
        return

    # pruning
    if prob <= result:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            # 재귀호출
            probability(row + 1, prob * (works[row][i] / 100))
            # 백트래킹
            visited[i] = False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    works = []
    for _ in range(N):
        person = list(map(int, input().split()))
        works.append(person)

    visited = [False] * N
    prob = []
    result = float('-inf')
    probability(0, 1.0)
    print(f'#{test_case} {result * 100:.6f}')
