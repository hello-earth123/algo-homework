T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    numbers.sort()
    result = []

    for i in range(N // 2 + 1):  # 짝수/홀수 대비
        if len(result) >= 10:
            break
        result.append(numbers[-(i + 1)])  # 큰 수
        if len(result) >= 10:
            break
        result.append(numbers[i])        # 작은 수

    print(f'#{test_case}', *result[:10])



# 이걸 셀렉션 알고리즘으로 풀 수는 없나


# T = int(input())

# for test_case in range(1, T+1):

#     N = int(input())

#     numbers = list(map(int, input().split()))
 

#     # 특별 정렬
#     for j in range(N-1):
#         for i in range(N//2):
#             numbers[i+j], numbers[(N-1)-i] = numbers[(N-1)-i], numbers[i+j]


#     print(f'#{test_case}', end = ' ')
#     for i in range(10):
#         print(f'{numbers[i]}', end = ' ')
#     print()