def calc(ingredients):
    for i in range(len(ingredients)):
        for j in range(i + 1, len(ingredients)):
            total += synerge_table[ingredients[i]][ingredients[j]]
            total += synerge_table[ingredients[j]][ingredients[i]]
    return total

def dfs(idx, cnt):
    global result
    if cnt == N // 2:
        A, B = [], []
        for i in range(N):
            if visited[i]:
                A.append(i)
            else:
                B.append(i)
        sum_A = calc(A)
        sum_B = calc(B)
        result = min(result, abs(sum_A - sum_B))
        return
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, cnt + 1)
            # backtracking
            visited[i] = False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())    # 노드의 갯수
    synerge_table = []
    for _ in range(N):
        row = list(map(int, input().split()))
        synerge_table.append(row)
    visited = [False] * N
    result = float('inf')

N = int(input())
print(N % 20000303)