A = list(set(range(1,13)))

T = int(input())


# 비트 마스킹을 통해 부분집합을 만들어보자
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    
    # 조건을 만족하는 부분집합의 갯수
    result = 0

    # 총 부분 집합 모두 완성
    for i in range(1<<len(A)):   # 1<<len(A)는 부분집합의 갯수 / i번재 부분집하 
        # 부분집합 표현
        count = 0
        # 부분집합의 원소의 합 
        total = 0
        
        # 부분 집합 하나 완성 하는 덩어리
        for j in range(len(A)):  # 원소의 갯수만큼 비트 비교 / 
            if i & (1<<j): # &는 비트 연산자

                total += A[j]
                count += 1

        if count == N and total == K:
            result += 1


    print(f'#{test_case} {result}')