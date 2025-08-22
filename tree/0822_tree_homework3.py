# 트리 탐색
def tree(root):
    # 안에 리스트가 비어 있지 않으면
    if left_child[root]:
        tree(left_child[root][0])
    # 해당 노드(루트) 안에 들어 있는 단어 출력
    print(alphabet[root][0], end='')
    # 안에 리스트가 비어 있지 않으면
    if right_child[root]:
        tree(right_child[root][0])
    
for test_case in range(1, 11):
    # 정점의 갯수
    N = int(input())

    # 왼, 오 자식 리스트 생성
    left_child = [[] for _ in range(N+1)] 
    right_child = [[] for _ in range(N+1)]
    
    # 해당 노드안에 있는 알파벳
    alphabet = [[] for _ in range(N+1)] 

    # 트리 생성
    for _ in range(N):
        # 0 : 노드 번호
        # 1 : 알파벳 정보
        # 2 : 왼쪽 자식 노드
        # 3 : 오른쪽 자식 노드
        info = list(map(str, input().split()))
        alphabet[int(info[0])].append(info[1])
        # 왼쪽 자식 노드 있다면 넣기
        if len(info) ==3 or len(info) == 4:
            left_child[int(info[0])].append(int(info[2]))
        # 오른쪽 자식 노드 있다면 넣기
        if len(info) == 4:
            right_child[int(info[0])].append(int(info[3]))
    # print(alphabet)
    # print(left_child)
    # print(right_child)

    print(f'#{test_case}', end=' ')
    tree(1)
    print()