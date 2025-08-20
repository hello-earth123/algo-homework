for test_case in range(1, 11):
    N = int(input())

    calc = list(map(str, input()))



    stack = []
    for c in calc:
        if len(stack) == 2:
            a = stack.pop()
            b = stack.pop()
            result = a + b
            stack.append(result)


        if c.isdigit():
            stack.append(int(c))
        elif c == '+':
            continue

            

    print(f'#{test_case} {stack.pop(-2)+stack[-1]}')