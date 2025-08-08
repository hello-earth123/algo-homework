T = int(input())

for test_case in range(1, T+1):

    str1 = input()
    str2 = input()
    count  = 0
    total = 0

    # 문자열 순회
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count += 1
        if count > total:
            total = count
        count = 0

    print(f'#{test_case} {total}')