T = int(input())
def merge(left, right):
    result = [0] * (len(left) + len(right))
    l = r = 0 # 인덱스 번호

    # 쪼개진 리스트를 각각의 l, r 포인터를 통해 가리키면서
    # left[l]과 right[r] 중에 더 작은 값이 먼저 result에 들어간다.
    # 그 후 더 작은 값이 들어간 리스트의 포인터는 한 칸 앖으로 이동(서바이벌 형식 처럼)
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # 왼쪽 리스트에 남은 데이터들을 모두 result에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1
    # 오른쪽 리스트에 남은 데이터들을 모두 result에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result

def merge_devide_sort(lst):
    # 리스트 길이 하나 되면 분할 종료
    if len(lst) == 1:
        return lst

    # 반씩 쪼개기
    mid = len(lst) // 2
    left = lst[:mid] # 쪼갠 왼쪽 리스트
    right = lst[mid:] # 쪼갠 오른쪽 리스트

    # 쪼갠 왼쪽 오른쪽 리스트들이 각각 다시 부모 리스트(?)가 되어 쪼개짐
    left_list = merge_devide_sort(left)
    right_list = merge_devide_sort(right)

    # 분할 끝났으면 병합하기
    merged_list = merge(left_list, right_list)
    return merged_list






for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    sorted_numbers = merge_devide_sort(numbers)
    print(f'#{test_case}', end = ' ')
    print(*sorted_numbers)
    