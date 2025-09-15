# 일단 덩어리 만들기
def make_set(n):
    parents = [i for i in range(n + 1)]
    return parents

# 대표자 찾기 함수
def find_set(x):
    # 자기 자신이면 되돌아가기
    if x == parents[x]:
        return parents[x]
    
    # compression
    parents[x] = find_set(parents[x])
    return parents[x]

# 덩어리로 합치기 함수
def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    parents = make_set(N)
    # union 합치기
    for _ in range(M):
        person1, person2 = map(int, input().split())
        union(person1, person2)
    # 대표자 최종 찾기
    for i in range(1, N + 1):
        find_set(i)

    parents = set(parents) - {0}
    result = len(parents)
    print(f'#{test_case} {result}')