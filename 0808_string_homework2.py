# 거꾸로 읽어도 똑같은 문장을 회문이라고 한다.
# 회문이면 1, 아니면 0
# 3 <= 단어 길이 <= 10


T = int(input())

for test_case in range(1, T+1):
    # 단어 입력
    char = input()


    #회문 체크
    for idx in range(len(char)//2+1):

        if char[idx] == char[-1-idx]:
            result = 1
        # 회문 아니면 종료
        else:
            result = 0
            break


    print(f'#{test_case} {result}')