# 주사위 3개 던져서 합이 10이하인 경우
cnt = 0
for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            if a + b + c <= 10:
                cnt += 1

path = []
result = 0

def recur(cnt):
    global result
    
    if cnt == 3:
        print(*path)
        if sum(path) <= 10:
            result += 1
        return
    
    for num in range(1, 6):
        path.append(num)
        recur(cnt + 1)
        path.pop()


# 시간 복잡도를 줄이는 방법
# 1. 가지치기
# 2. append 사용하지 않기
def recur(cnt, total):
    global result
    
    # 이미 10을 넘은 경우는 더 볼 필요가 없다.
    # 기저 조건에서 많은 경우의 수들을 줄일 수 있따.
    if total > 10:
        return
    
    if cnt == 3:
        # if total <= 10:   # 여기까지만 생각해도 오케이
            # result += 1
        result += 1         # 효율적인 코드
        return
    
    for num in range(1, 7):
        # 누적해 나아가야 한다면, 파라미터로 만들어서 재귀 호출 시에 합을 계속 더해준다.
        recur(cnt + 1, total + num)

recur(0)