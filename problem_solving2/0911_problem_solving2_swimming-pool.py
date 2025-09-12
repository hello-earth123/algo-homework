# 1일권 -> 1일 이용
# 1달 이용권 -> 1달 이용 (매 달 1일 부터 시작)
# 3달 이용권 -> 다음 해의 이용권만 구매 (연속된 3달만 가능)
# 1년 이용권 -> 매 년 1월 1일부터 시작
# 가장 적은 비용으로 수영장 이용

T = int(input())
for test_case in range(1, T + 1):
    costs = list(map(int, input().split()))
    use = list(map(int, input().split()))
    
    # dp의 상태: 개월 수
    # dp의 값: 총 돈의 값
    dp = [0] * 13

    for i in range(1, 13):
        # 1일권 vs 1달권
        dp[i] = min((dp[i - 1] + use[i - 1]* costs[0]), (dp[i - 1] + costs[1]))

        # 3달권과 3달권 안사용했을 때 비교
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + costs[2])

    # 1년권과 1년권 안사용했을 때 비교
    result = min(dp[12], costs[3])

    print(f'#{test_case} {result}')