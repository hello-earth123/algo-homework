# 동전의 최소 갯수
# 규칙 : 큰 동전부터 나누자 (다 나눴으면 빼서 버려)
coin_list = [100, 50, 500, 10]
target = 1730
cnt = 0
result = 0

# Greedy 문제의 단골 손님
# 정렬 연습 : 튜플이라면? 인스턴스 리스트? 역순이라면?
#       - 예) 길이가 우선 정렬, 같은 길이는 사전 순으로 정렬
# list.sort() vs sorted()
# 정렬을 통해 먼저 계산하고 버리고 계산하고 버리고
coin_list.sort(reverse=True) # 큰 동전부터 사용

for coin in coin_list:
    possible_cnt = target // coin # 현재 동전으로 가능한 최대 수
    result += possible_cnt        # 정답에 더해준다.
    target -= coin * possible_cnt # 금액을 빼준다.
print(result)

# 그리디는 구현은 어렵지 않다.
# 규칙을 찾는 것이 어려울 뿐
# 숨겨진 규칙을 잘 찾아야 한다. (힌트 : 정렬 같은거)
