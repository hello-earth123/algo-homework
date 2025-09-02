T = int(input())

for test_case in range(1, T+1):
    n = float(input())
    result = ''
    overflow = False

    for i in range(12):  # 최대 12자리까지만
        n *= 2
        if n >= 1:
            result += '1'
            n -= 1
        else:
            result += '0'

        if n == 0:   # 딱 떨어지면 변환 끝
            break
    else:
        # for문이 정상 종료되면 12자리 안에 못 끝남
        overflow = True

    if overflow:
        print(f'#{test_case} overflow')
    else:
        print(f'#{test_case} {result}')


# | 단계 | n * 2 | 정수 | 소수 남음 | result |
# | -- | ------ | -- | ----- | ------ |
# | 1  | 1.25   | 1  | 0.25  | 1      |
# | 2  | 0.5    | 0  | 0.5   | 10     |
# | 3  | 1.0    | 1  | 0.0   | 101    |

# 어떤 수를 나눴을 때 그 나머지가 뒤에서부터 채워지는게 이진수
# 소수의 이진수는 완전 반대
# 어떤 수를 곱했을 때 그 몫이 앞에서부터 채워지는게 이진수