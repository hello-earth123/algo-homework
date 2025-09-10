# 이진 탐색 -> # 이진 검색을 하기 위해서는 반드시 자료가 정렬된 상태여야함
# a는 리스트, N은 리스트 요소 갯수(리스트 길이)
def binarySearch(a, N, key): # key를 찾으면 인덱스, 실패하면 -1을 반환
    # 시작과 끝은 모두 인덱스 번호를 기준으로 설정한다.
    start = 0
    end = N-1
    count = 0
    while start <= end:
        middle = (start + end) // 2

        if a[middle] == key: # 검색 성공
            return middle, count

        elif a[middle] > key: # 찾는 값보다 크면
            count += 1
            end = middle -1     # 왼쪽 구간 선택
        
        else:
            count += 1
            start = middle + 1
    
    return -1, count

# 여기서 count는 이진 탐색을 이행한 횟수를 의미한다.
