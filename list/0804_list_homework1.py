#디지털 필터링의 기본
T = int(input())


for test_case in range(1, T+1):
    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))
    

    # 최대 최소를 찾기 위한 초기값
    result_max = float('-inf')
    result_min = float('inf')
    


    #최대, 최소값 업데이트
    for i in range(N-M+1):
            numbers_total = sum(numbers[i:i+M])       

            if numbers_total > result_max:
                result_max = numbers_total
    

            if numbers_total <= result_min:
                result_min = numbers_total
                

    print(f'#{test_case} {result_max - result_min}')