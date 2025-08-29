# 완전 이진 트리를 유지
# 부모 < 자식 (min heap 유지)

T = int(input())

def bst(n):
    global last
    last += 1
    tree[last] = n

    c = last
    p = c // 2

    while p and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2


for test_case in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    arr = list(map(int, input().split()))
    last = 0
    total = 0
    for i in range(len(arr)):
        bst(arr[i])
    # print(tree)


    child = last
    parent = child // 2
    while parent > 0:
        total += tree[parent]
        child = parent
        parent = child // 2

    print(f'#{test_case} {total}')
