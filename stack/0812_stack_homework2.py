T = int(input())

pair = {
    ')' : '(',
    '}' : '{',
    ']' : '[',
    '>' : '<',
}


for test_case in range(1, T+1):

    char = input()
    parenthesis = []
    result = 1

    for c in char:
        # 여는 괄호 push
        if c in '({[<':
            parenthesis.append(c)
        
        # 괄호 쌍 안맞으면 0
        elif c in ')}]>':
            if (not parenthesis) or (parenthesis[-1] != pair[c]):
                result = 0
                break
            parenthesis.pop()
    
    # 다 돌았는데 안비어 있으면 0
    if parenthesis:
        result = 0

    print(f'#{test_case} {result}')