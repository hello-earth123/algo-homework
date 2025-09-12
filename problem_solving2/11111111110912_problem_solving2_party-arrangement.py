# 참여 할지, 말지
# 공집합 제외
# 내일도 활동하면 열쇠 념겨줌
# 다 끝나면 열쇠 아무나 가져
# 책임자는 무조건 참여
# A, B, C, D 네 명
dic = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
}
T = int(input())
for test_case in range(1, T + 1):
    charge = input()
    N = len(charge)
    result = 1

    if charge[0] == charge[1]:
        if charge[0] == 'A':
            result *= (2 ** 6)
    elif charge[0] == charge[1]:
        if charge[0] != 'A':
            result *= 2 ** 5
    if charge[0] != charge[1]:
        if charge[0] != 'A':
            result *= ((2 ** 5) - 3)
    elif charge[0] != charge[1]:
        if charge[0] == 'A':
            result *= ((2 ** 6) - 9)

    for i in range(1, N - 1):
        if charge[i] == charge[i + 1]:
            result *= (2 ** 6)
        else:
            result *= ((2 ** 6) - 9)

    print(f'#{test_case} {result % 1000000007}')
