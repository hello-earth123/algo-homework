arr = ['O', 'X']
name = ['MIN', 'CO', 'TIM']
path = []

def recur(cnt):
    # 종료조건 (3명을 모두 고려)
    if cnt == 3:
        print(*path)
        return

    # 재귀호출 파트
    # - 부분집합에 포함 되는 경우 (O를 추가)
    path.append(arr[0])
    recur(cnt + 1)
    # 마지막 O를 포함하기 전으로 돌아간 후에
    path.pop()


    # - 포함되지 않는 경우 (X를 추가)
    path.append(arr[1])
    recur(cnt + 1)
    # 마지막 X를 포함하기 전으로 돌아간 후에
    path.pop()

recur(0) # 0명을 고려한 상태로 시작


# ------------------------ 실제 많이 보게될 코드

name = ['MIN', 'CO', 'TIM']

# 두 번째 선택 에서는
# 'MIN'이라는 친구가 포함된 상태를 저장하면서
def recur(cnt, subset):
    if cnt == 3:
        print(*subset)
        return
    
    # 부분집합에 포함 시키는 경우
    recur(cnt + 1, subset + [name[cnt]])
    # 포함 시키지 않는 경우
    recur(cnt + 1, subset)

recur(0, [])

# 재귀 호출 시에 subset + [name[cnt]] 이거랑 subset은 
# 같은 주소 값을 가지지 않는다. 
# subset += [name[cnt]] 이렇게 하면 같은 주소 값을 가진다.
