# 두 개 선택해서 정해진 횟수만큼 자리 교체 가능
# 교환 횟수만 맞추면 됨

# 가장 큰 금액 계산


def my_score(cnt):
    global nums, length
    # 종료 조건
    if cnt == N:
        return
    
    # swap하고 cnt 하나 늘리기
    tmp = set()
    for num in nums:
        # print(num)
        for i in range(length - 1):
            for j in range(i + 1, length):
                t = [n for n in num]
                t[i], t[j] = t[j], t[i]
                tmp.add(''.join(t))
    nums = tmp
    # print(nums)
    my_score(cnt + 1)

T = int(input())
for test_case in range(1, T + 1):
    num, N = input().split()
    N = int(N)
    length = len(num)
    nums = set()
    nums.add(num)

    my_score(0)

    print(f'#{test_case} {max([int(n) for n in nums])}')