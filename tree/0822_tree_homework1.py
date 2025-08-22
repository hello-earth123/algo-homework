# L -> V -> R 순서의 중위
T = int(input())

# root는 root, N은 노드의 갯수
def tree_inorder(root, N):
    global num
    # 유도 조건
    if root <= N:
        tree_inorder(root*2, N)     # 왼쪽 자식
        tree[root] = num            # 현재 노드 채우기 (위치에 따라 전위, 중위, 후위 결정)
        num += 1                    # 숫자 증가 
        tree_inorder(root*2+1, N)   # 오른쪽 노드

for test_case in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    num = 1
    tree_inorder(1, N)

    print(f'#{test_case} {tree[1]} {tree[N//2]}')