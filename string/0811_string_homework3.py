T = int(input())
for test_case in range(1, T+1):
    
    A, B = map(str, input().split())

    # 타이핑 세기
    count = 0
    
    if B in A:
        new_char = A.replace(B, '')
        count += (len(A)-len(new_char)) // len(B)
    
        
    # print(A)
    count += len(new_char)

    print(f'#{test_case} {count}')