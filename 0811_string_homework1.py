T = int(input())
 
for test_case in range(1, T+1):
    N = input()
    M = input()
 
    result = 0
    if N in M:
        result = 1
    else:
        result = 0
 
    print(f'#{test_case} {result}')