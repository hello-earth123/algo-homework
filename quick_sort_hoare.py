arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
# arr = [11, 45, 23, 81, 28, 34]
# arr = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
# arr = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# pivot: 제일 왼쪽 요소
# 이미 정렬된 배열이나 역순으로 정렬된 배열에서 최악의 성능을 보일 수 있음
# 0 ~ j까지는 pivot보다 작은 수가, j+1부터 N-1까지는 pivot보다 큰 수가 와야한다.
# 그 후 j 인덱스에 pivot이 들어간다.
# i는 pivot 보다 더 큰 값을 찾는다.
# j는 pivot 보다 더 작을 값을 찾는다.
def hoare_partition1(left, right):
    pivot = arr[left] # pivot을 제일 왼쪽 요소로 설정
    i = left + 1
    j = right

    while i <= j:   # 교차가 되면 끝
        while i <= j and arr[i] <= pivot:   # i는 pivot보다 큰 값을 검색 (작거나 같으면 i += 1)
            i += 1

        while i <= j and arr[j] >= pivot:   # j는 pivot보다 작은 값을 검색 (크거나 같으면 j -= 1)
            j -= 1

        if i < j: # swap
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

# pivot: 제일 오른쪽 요소
def hoare_partition2(left, right):
    pivot = arr[right]  # pivot을 제일 오른쪽 요소로 설정
    i = left
    j = right - 1

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
    
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[right] = arr[right], arr[i]
    return i

# pivot: 중간 요소
def hoare_partition3(left, right):
    mid = (left + right) // 2
    pivot = arr[mid] # pivot을 중간 요소로 설정
    arr[left], arr[mid] = arr[mid], arr[left] # 중간 요소를 왼쪽으로 이동 (필요 시)
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j


