from collections import deque
for _ in range(1, 11):
    test_case = int(input())

    numbers = deque(list(map(int, input().split())))
    i = 1
    while True:
        # 사이클 초기화
        if i == 6:
            i = 1
        # 종료 조건
        if numbers[0] - i <= 0:
            numbers[0] = 0
            numbers.rotate(-1)
            break

        numbers[0] -= i
        numbers.rotate(-1)

        # 사이클 증가
        i += 1

    print(f'#{test_case}')
    for num in numbers:
        print(num, end=' ')
    print()
    