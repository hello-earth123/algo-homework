def make_set(n):
    parents = [i for i in range(n + 1)]
    return parents

def find_set(x):
    if x == parents[x]:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    global cnt
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return
    
    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y
    

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 각 집합 만들기
    parents = make_set(N)

    # 지목한 사람들 끼리 합치기
    for i in range(0, len(arr) - 1, 2):
        union(arr[i], arr[i + 1])
    # print(parents)
    
    for i in range(1, N + 1):
        find_set(i)

    # 중복 제거
    parents = set(parents)
    # print(parents)
    # 0은 제외
    result = len(parents) - 1
    print(f'#{test_case} {result}')