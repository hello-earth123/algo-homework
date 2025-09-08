arr = [1, 2, 3, 4]

# # i : 0~2^n == i 번째 부분집합
# for i in range(1 << len(arr)):
#     for idx in range(len(arr)):
#         if i & (1 << idx):
#             print(arr[idx], end = " ")
#     print()



# 맨 오른쪽만 검사 하면서 shift 연산을 통해 하나씩 없애준다.
# 검사하고자 하는 비트를 오른쪽으로 하나씩 shift 하면서 체크하는 코드
n = len(arr)

def get_sub(tar):
    print(f'target = {tar}', end = '/')
    for i in range(n):
        # 0x1로 표기한 이유 (사실 1, 0b1, 0b0001 True 다 됨)
        # - 비트 연산임을 명시하는 권장 방법
        if tar & 0x1:   # 가장 우측 비트를 체크
            print(arr[i], end = ' ')
        tar >>= 1

for target in range(1 << n):
    get_sub(target)
    print()