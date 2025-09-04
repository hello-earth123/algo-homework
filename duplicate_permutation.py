# # 중복 순열
# # [0, 1, 2] 3개의 카드가 존재 -> 2개를 뽑는다.
# path = []
# used = [False] * 7  # 고를 수 있는 수 만큼 만들어준다.

# # 기저조건 (종료조건) : 2개의 카드를 모두 뽑았다면 종료
# # - 시작점 : 0개의 카드를 고른 상태부터 시작
# # 다음 재귀호출 구조 : [0, 1, 2] 카드 중 하나를 고른다.


# def recur(cnt):
#     # 기저 조건
#     if cnt == 3:
#         print(*path)
#         return
    
#     for num in range(1, 7):
#         # 중복 제거
#         if used[num]:     # 이미 path에 있는 숫자는 생략
#             continue        # in은 iteration을 모두 확인하기 때문에 굉장히 느림
        
#         # 사용 여부 체크
#         used[num] = True                   
#         path.append(num)
#         recur(cnt + 1)
#         path.pop()
#         # 초기화
#         used[num] = False

#     # # 카드 0, 1, 2 중 하나를 선택
#     # path.append(0)
#     # recur(cnt + 1) # 하나 선택했으니 다음 선택으로 이동
#     # path.pop()

#     # path.append(1)
#     # recur(cnt + 1)
#     # path.pop()

#     # path.append(2)
#     # recur(cnt + 1)
#     # path.pop()

# recur(0)


