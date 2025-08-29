def calc(node):
    value = tree[node][0]
    # 숫자 노드면 반환
    if value not in '+-*/':
        return int(value)
    
    # 연산자 노드면 재귀적으로 왼쪽, 오른쪽 값 구하기
    else:
        left, right = tree[node][1], tree[node][2]
        l_val, r_val = calc(left), calc(right)
    
    if value == '+':
        return l_val + r_val
    elif value == '-':
        return l_val - r_val
    elif value == '*':
        return l_val * r_val
    elif value == '/':
        return l_val // r_val   # 문제에서 정수 나눗셈
    
T = 10
for test_case in range(1, T+1):
    N = int(input())
    tree = {}

    for _ in range(N):
        arr = input().split()
        node = int(arr[0])
        if len(arr) == 2:
            tree[node] = [arr[1]]  # 숫자
        else:
            tree[node] = [arr[1], int(arr[2]), int(arr[3])]  # 연산자, 왼쪽, 오른쪽

    result = calc(1)
    print(f"#{test_case} {result}")















import operator
# 정점에 연산자가 있으면
# 왼쪽과 오른쪽 서브트리의 결과에 해당 연산자를 적용
op = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv,
}

node = 1
def preorder(root):
    '''
    L -> V -> R
    '''
    global node
    if tree[root] in '+-*/':
        node += 1
        preorder(node)


for test_case in range(1, 2):
    # root부터 순회하면서 연산자가 나오면 이동
    # 자식이 없거나 연산자가 없으면 연산 진행
    N = int(input())    # 정점의 갯수
    tree = [''] * (N + 1)
    lft_child = [0] * (N + 1)
    rgt_child = [0] * (N + 1)
    for _ in range(N):
        data = input().split()
        # 만약 사칙 연산이라면
        if data[1] in '+-*/':
            tree[int(data[0])] = data[1]
            tree(data[2]), tree(data[3])

        # 만약 숫자라면
        else:
            tree[int(data[0])] = data[1]

        # 트리 순회인가..?

            
    # print(data)    
    print(tree)
    print(f'#{test_case} {tree[1]}')