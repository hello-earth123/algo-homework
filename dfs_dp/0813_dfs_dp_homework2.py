# 작은 문제를 기반으로 규칙성을 찾아 큰 문제를 해결한다. (DP)
# 특정 조건을 두어 규칙성을 좀 더 쉽게 찾을 수 있다.
T = int(input())
for test_case in range(1, T+1):
    dp = [0] * 301
    dp[10] = 1
    dp[20] = 3
    for i in range(30, len(dp)):
        dp[i] = dp[i-10] + (dp[i-20] * 2)
    
    result = dp[int(input())]

    print(f'#{test_case} {result}')
