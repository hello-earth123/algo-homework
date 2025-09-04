# A, J, Q, K가 충분히 있따.
# 5장 뽑을 때 같은 종류의 카드가 3장 연속으로 나오는 경우의 수

cards = ['A', 'J', 'Q', 'K']
path = []
result = 0
# 연속된 3개의 같은 카드가 나오면 return True, 아니면 False
def count_three():
    if path[0] == path[1] == path[2]: return True
    if path[0] == path[1] == path[2]: return True
    if path[0] == path[1] == path[2]: return True
    return False

def recur(cnt):
    global result

    if cnt == 5:
        # Todo: 연속된 3개가 나오면 counting
        if count_three():
            result += 1
        return
    
    # 4개의 카드 중 하나를 선택
    for idx in range(len(cards)):
        path.append(cards[idx])
        recur(cnt + 1)
        path.pop()
        
recur(0)