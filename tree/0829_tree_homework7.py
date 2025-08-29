# 완전이진트리
# 부모 > 자식 : 최대 힙 (루트가 제일 큼)
# 부모 < 자식 : 최소 힙 (루트가 제일 작음)

# 연산1 : 삽입
# 연산2 : 삭제 (최대값 출력 후 그 값 삭제) 최대 힙의 루트 노드 출력 후 삭제 한다는 뜻
T = int(input())

def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c // 2
    while (p > 0) and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2

def deq(n):
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1
    p = 1
    c = p * 2
    while c <= last:
        if c + 1 <= last and tree[c] < tree[c + 1]: # 오른쪽 자식 존재하면서 왼쪽 자식보다 오른쪽 자식이 더 크다면
            c += 1                                  # 오른쪽 자식을 비교 대상으로 설정
        if tree[p] < tree[c]:                       # 부모와 자식 비교 (오른쪽 자식이 더 크면 오른쪽 자식, 아니면 원래대로 왼쪽 자식)
            tree[p], tree[c] = tree[c], tree[p]
            p = c                                   # 자식이 부모가 되고
            c = p * 2                               # 더 밑에 있는 친구가 자식이 된다.(완전 이진 트리에서는 부모*2가 왼쪽 자식, 부모*2+1이 오른쪽 자식)
        else:
            break
    return tmp                                      # max hea return

for test_case in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    last = 0
    result = []
    for _ in range(N):
        data = list(map(int, input().split()))
        if data[0] == 1:
            enq(data[1])

        else:
            if last < 1:                            # heap에 존재하는 모든 값들을 다 append했다면 last가 더이상 갈 곳이 없다면 여기서 last가 의미하는 것은 가장 마지막 노드를 뜻한다.
                result.append(-1)
            else:
                result.append(deq(tree[1]))

    print(f'#{test_case}', end = ' ')
    for i in range(len(result)):
        print(result[i], end = ' ')
    print()