# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    length, n = input().split()
    length = int(length)
    
    # 각 16진수 문자를 4자리 2진수로 변환
    binary_str = ""
    for ch in n:
        binary_str += format(int(ch, 16), "04b") # format은 출력 형식 format(숫자, "형식") 형식 : 04b -> 뒤에서부터 binary로 바꾼다. 4자리씩 끊는다. 빈 칸은 0으로 채운다.
    
    print(f'#{test_case} {binary_str}')
