import operator

T = int(input())
for test_case in range(1, T+1):
    calc = input().split()

    # 연산자 매핑
    calculation = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv  # 문제 조건: 정수 나눗셈
    }

    stack = []
    error_flag = False

    for c in calc:
        if c.isdigit():  # 숫자면 스택에 push
            stack.append(int(c))

        elif c in calculation:  # 연산자면
            if len(stack) < 2:  # 피연산자 부족
                print(f'#{test_case} error')
                error_flag = True
                break
            b = stack.pop()
            a = stack.pop()
            result = calculation[c](a, b)
            stack.append(result)

        elif c == '.':  # 수식 끝
            if len(stack) == 1:
                print(f'#{test_case} {stack.pop()}')
            else:
                print(f'#{test_case} error')
            break

    # '.' 없이 끝난 경우
    if not error_flag and calc[-1] != '.':
        print(f'#{test_case} error')
