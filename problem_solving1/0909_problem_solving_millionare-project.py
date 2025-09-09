T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    bargain = list(map(int, input().split()))
    
    # 최고점일 때를 기준으로 자른다.
    money = 0
    cnt = 0
    arr = []
    maximum = max(bargain)
    for i in range(len(bargain)):
        if bargain[i] < maximum:
            arr.append(bargain[i])
            bargain[i] = 0
        else:
            pass

        if bargain[i] == maximum:
            money -= sum(arr)
            money += maximum * len(arr)
            arr = []
            bargain[bargain.index(maximum)] = 0
            maximum = max(bargain)
    print(f'#{test_case} {money}')