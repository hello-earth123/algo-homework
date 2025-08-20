import operator
for test_case in range(1, 11):
    N = int(input())

    calc = list(map(str, input()))

    calculation = {
        '+' : operator.add,
        '*' : operator.mul,
    }

    stack = []
    stack_cal = []
    for c in calc:
        if stack_cal and stack_cal[-1] == '*':
            a = stack.pop()
            p = stack_cal.pop()
            result = calculation[p](a, int(c))
            stack.append(result)
        
        elif c.isdigit():
            stack.append(int(c))
        else:
            stack_cal.append(c)
            # print(stack_cal)    
    # print(stack)
    print(f'#{test_case} {sum(stack)}')

# 우선순위로 정렬 = 스택을 사용
# 우선순위가 더 높은것이 위로 쌓임 (LIFO의 성질)
# 우선순위가 더 낮은것이 오면 더 높은 것을 pop한다. -> 본인이 우선순위가 더 높을 때 까지
# 이 과정을 반복