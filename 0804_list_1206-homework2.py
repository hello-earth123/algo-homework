for test_case in range(1, 11):

    N = int(input())

    buildings = list(map(int, input().split()))

    result = 0
    # 0 0 3 6 2 5 9 0 6 4 0 6 0 0

    # 건물을 기준으로 왼쪽으로 한칸, 두칸이 모두 본인 보다 작은 수이고, 오른쪽도 본인 보다 작은 수가 연속되면
    # 그 차의 최솟값이 조망권이 확보된 건물

    for i in range(2, N-2):
        if (buildings[i] > buildings[i+1]) and (buildings[i] > buildings[i+2]) and (buildings[i] > buildings[i-1]) and (buildings[i] > buildings[i-2]):
            result += min(buildings[i]-buildings[i+1], buildings[i]-buildings[i+2], buildings[i]-buildings[i-1], buildings[i]-buildings[i-2])

    print(f'#{test_case} {result}')