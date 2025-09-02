# 암호코드는 숫자 8개
# 암호 코드에서 숫자 하나는 -> 7개의 비트로 이루어짐
# 암호코드 가로 길이는 56
# 올바른 암호코드는 홀수합*3 + 짝수합 = 10이 되어야 함
# 스캐너는 암호코드 하나를 포함한 직사각형 배열을 읽는다.
# 암호코드 이외의 부분은 전부 0

# from pprint import pprint
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())    # N: 세로, M: 가로

    keys = []
    for _ in range(N):
        row = input()
        keys.append(row[::-1])
    # pprint(keys)
    
    # 암호 시작지점 찾기
    found = False
    for r in range(N):
        for c in range(M):
            if keys[r][c] == '1':
                r_k, c_k = r, c
                found = True
                break
        if found:
            break
    # print(r_k, c_k)
    key_reversed = keys[r_k][c_k:c_k+56]
    key = key_reversed[::-1]
    # print(key)
    # key를 7자리씩 끊어서 계산
    odd = []
    even = []
    check = 1
    for i in range(0, 56, 7):
        key[i:i+7]
        if key[i:i+7] == '0001101':
            number = 0
        elif key[i:i+7] == '0011001':
            number = 1
        elif key[i:i+7] == '0010011':
            number = 2
        elif key[i:i+7] == '0111101':
            number = 3
        elif key[i:i+7] == '0100011':
            number = 4
        elif key[i:i+7] == '0110001':
            number = 5
        elif key[i:i+7] == '0101111':
            number = 6
        elif key[i:i+7] == '0111011':
            number = 7
        elif key[i:i+7] == '0110111':
            number = 8
        elif key[i:i+7] == '0001011':
            number = 9

        # print(number)
        if check % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
        check += 1
    
    if ((sum(odd) * 3) + sum(even)) % 10 == 0:
        result = (sum(odd) + sum(even))
    else:
        result = 0

    print(f'#{test_case} {result}')