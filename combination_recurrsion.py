# 5명 중 3명을 순서 없이 고르기
# 조합(combination)
arr = ['A', 'B', 'C', 'D', 'E']
N = 3
path = []

def recur(cnt, start):
    # N명 뽑으면 종료
    if cnt == N:
        print(*path)
        return
    
    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(cnt + 1, i + 1)   # i 번째를 골랐으니, 다음 선택은 i + 1부터 고려
        path.pop()              # 만약에 i + 1이 아니고 i 이면 중복 순열이 된다.

recur(0, 0)