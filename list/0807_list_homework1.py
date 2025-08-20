# 선택 정렬
# a는 리스트 / N은 리스트 안에 요소 갯수 (리스트의 길이)
def selection_sort(a, N):
    for i in range(N-1):            # 정렬 구간의 시작 인덱스
        min_idx = i                 # 첫 원소를 최소로 가정
        for j in range(i+1, N):
            if a[min_idx] > a[j]:   # 최소 원소 위치 갱신
                min_idx = j
        
        a[i], a[min_idx] = a[min_idx], a[i] # 구간 최솟값을 구간 맨 앞으로


# 버블 정렬
def bubble_sort(a, N):              # a는 정렬할 List, N은 원소 수 (N의 갯수)
    for i in range(N-1, 0, -1):     # 범위의 끝 위치
        for j in range(i):          # 비교할 왼쪽 원소 인덱스 j
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j] # 바로 뒤에 인덱스랑 비교해서 크면 뒤로 보내기


T = int(input())

for test_case in range(1, T+1):
    # 입력
    N = int(input())
    numbers = list(map(int, input().split()))

    # numbers 정렬하기
    selection_sort(numbers, N)

    # 출력
    print(f'#{test_case}', end = ' ')
    for number in numbers: 
        print(f'{number}', end = ' ')
    print()