V = int(input()) # 정점의 개수, 정점번호는 1번부터 V번까지
arr = list(map(int, input().split()))

lft_child = [0] * (V+1) # 1 ~ V까지 인덱스가 필요하므로
rgt_child = [0] * (V+1)

for i in range(V-1):
    # 부모 자식 부모 자식 부모 자식 .... 이렇게 주어지니까
    # 짝수번째 인덱스는 부모, 홀 수번째 인덱스는 자식이 된다.
    parent, child = arr[2*i], arr[2*i + 1]
    print(parent, child)
    if lft_child[parent] == 0:
        lft_child[parent] = child
    else:
        rgt_child[parent] = child

print(lft_child)
print(rgt_child)
# 트리 저장 완료


def f(root):
    # root : 현재 탐색하고 있는 트리의 루트 노드
    print(root, end=' ')
    # 유도 조건
    # 자식이 있다면, 해당 자식을 중심으로 순회
    if lft_child[root] != 0: # 왼쪽 자식이 있다면
        f(lft_child[root])
    if rgt_child[root] != 0: # 오른쪽 자식이 있다면
        f(rgt_child[root])

# 중위순회
def inorder(root):
    # root : 현재 탐색하고 있는 트리의 루트 노드
    
    # 유도 조건
    # 자식이 있다면, 해당 자식을 중심으로 순회
    if lft_child[root] != 0: # 왼쪽 자식이 있다면
        inorder(lft_child[root])

    print(root, end=' ')

    if rgt_child[root] != 0: # 오른쪽 자식이 있다면
        inorder(rgt_child[root])


# 후위순회
def postorder(root):
    # root : 현재 탐색하고 있는 트리의 루트 노드
    
    # 유도 조건
    # 자식이 있다면, 해당 자식을 중심으로 순회
    if lft_child[root] != 0: # 왼쪽 자식이 있다면
        postorder(lft_child[root])

    if rgt_child[root] != 0: # 오른쪽 자식이 있다면
        postorder(rgt_child[root])    

    print(root, end=' ')


# 트리의 순회
# 재귀함수의 설계
print("트리 전위순회 시작")
f(1) # 1번 노드를 중심으로 순회
print()
print("트리 전위순회 끝")

print("트리 중위순회 시작")
inorder(1) # 1번 노드를 중심으로 순회
print()
print("트리 중위순회 끝")

print("트리 후위순회 시작")
postorder(1) # 1번 노드를 중심으로 순회
print()
print("트리 후위순회 끝")