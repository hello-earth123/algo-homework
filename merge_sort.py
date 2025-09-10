# 1. 분할
# 2. 정복 & 병합(정렬)
def merge(left, right):
    # 두 리스트를 병합할 최종 리스트
    result = [0] * (len(left) + len(right))
    l = r = 0    # 인덱스

    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]



def merge_sort(li):
    # 쪼갤 리스트의 길이가 1이면 stop
    if len(li) == 1:
        return li
    
    # 절반 씩 분할하여 출력해라
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]
    # print(left, right)

    # 이진트리랑 비슷하네
    left_list = merge_sort(left)
    right_list = merge_sort(right)
    
    # 병합
    merge_list = merge(left_list, right_list)
    return merge_list

arr = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)
print(sorted_arr)


arr = list(map(int, input().split()))

# 병합정렬 구현
# 1. 두 부분으로 나누기 : merge_sort()
# 2. 나눠지 두 부분을 합치기 : merge()

def merge_sort(left, right):    # 구간 [left, right)
    if left + 1 == right:   # 구간에 포함된 원소가 1개일 때
        return              # 종료
    
    if left + 1 < right:    # 구간에 포함된 원소가 2개 이상일 때
        # 분할하기
        mid = (left + right) // 2
        merge_sort(left, mid)   # mid 포함 X
        merge_sort(mid, right)  #  mid 포함 O

def merge_sort2(left, right):   # 구간 [left, right]
    if left == right:
        return
    
    if left < right:
        mid = (left + right) // 2
        merge_sort2(left, mid)  # mid 포함 X
        merge_sort2(mid + 1, right) # mid 포함 O

N = 8
merge_sort(0, N)    # [0, N) 구간을 둘로 쪼갠다.(길이가 1인 배열이 될 때 까지)
