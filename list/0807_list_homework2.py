# 이진 탐색 -> # 이진 검색을 하기 위해서는 반드시 자료가 정렬된 상태여야함
# a는 리스트, N은 리스트 요소 갯수(리스트 길이)
# key를 찾으면 인덱스, 실패하면 -1을 반환
def binary_search(p, key):
    start = 1
    end = p
    count = 0

    while start <= end:
        count += 1
        mid = (start + end) // 2
        if mid == key:
            return count
        elif mid > key:
            end = mid
        else:
            start = mid
    return count

T = int(input())
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())

    a_count = binary_search(P, A)
    b_count = binary_search(P, B)

    if a_count < b_count:
        winner = 'A'
    elif a_count > b_count:
        winner = 'B'
    else:
        winner = '0'

    print(f'#{test_case} {winner}')
