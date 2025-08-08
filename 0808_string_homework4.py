# z
# o
# tt
# ff
# ss
# e
# n
T = int(input())

# 순서
order = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for _ in range(T):

    test_case, length = input().split()
    arr = input().split()

    # count = {key : 0) 형태의 딕셔너리 생성
    # key('ZRO', 'ONE', 'TWO', 'THR', ....) / value (0) 으로 맞춘다.
    count = {key : 0 for key in order}
    for word in arr:
        count[word] += 1

    print(test_case)
    for word in order:
        print((word + ' ') * count[word], end='')
    print()

# 리스트 안에 들어있는 숫자의 갯수 만큼 딕셔너리 업데이트 (숫자 세기)
# order라는 이미 순서가 정해져 있는 뼈대가 있음
# 딕셔너리 숫자 * order만 해서 출력하면 끝