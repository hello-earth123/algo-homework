T = int(input())

# 트리
def tree(root):
    global num 
    # 유도 조건
    # 왼 -> 오 자식 노드가 존재하면 재귀 호출(이동)
    num += 1
    if left_child[root]:
        tree(left_child[root])

    if right_child[root]:
        tree(right_child[root])
        
for test_case in range(1, T+1):
    num = 0
    # E는 간선의 갯수, N은 노드의 번호(루트가 되는)
    # N이 트리의 노드
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    # E는 간선의 갯수 / E+1은 노드의 갯수 / E+2는 자식 번호
    left_child = [0] * (E+2)
    right_child = [0] * (E+2)

    # 이진 트리 만들기
    for i in range(E):
        parent, child = arr[i*2], arr[i*2 + 1]
        # 왼쪽 비어 있으면 왼쪽 자식
        if left_child[parent] == 0:
            left_child[parent] = child

        # 왼쪽 차 있으면 오른쪽 자식
        else:
            right_child[parent] = child

    # root를 기준으로 서브 트리 탐색
    tree(N)
    # 탐색 완료 후 결과 출력
    print(f'#{test_case} {num}')


# 트리 함수 (탐색)
'''
만약에 왼쪽 혹은 오른쪽 자식 노드가 존재 한다면 재귀 호출
'''

# 이진 트리 만들기
'''
노드의 갯수만큼 순회하면서
짝수는 부모, 홀수는 자식의 형태를 띈다 (입력 방법에 따라서 다를 수 있음)

왼쪽 자식, 오른쪽 자식 리스트 생성(노드의 갯수 + 1만큼 생성한다.)(번호 그대로 쓰기 위해)
해당 루트에 대해 왼쪽 자식이 비어있다면(left_child[root] == 0) 채우기
아니면(채워져 있다면) 오른쪽 자식에 채우기
이러면 완전 이진 트리 완성
'''