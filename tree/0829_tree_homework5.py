# N개의 노드
# 완전 이진 트리
# 같은 레벨에서 왼 -> 오 증가
# 다 차면 다음레벨로

T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split()) # 노드 갯수, 리프 노드 갯수, 값 출력할 노드 번호
    
    tree = [0] * (N + 1)

    for _ in range(M):
        leaf, num = map(int, input().split())
        tree[leaf] = num
    # print(tree)
    
    while N > 1:
        if N % 2 != 0:
            lft_child = tree[N-1]
            rgt_child = tree[N]

            parent = lft_child + rgt_child
            tree[(N - 1) // 2] = parent
            N -= 2
        else:
            tree[N // 2] = tree[N]

            lft_child = tree[N-2]
            rgt_child = tree[N-1]
            parent = lft_child + rgt_child
            tree[(N - 2) // 2] = parent
            N -= 3

    print(f'#{test_case} {tree[L]}')  