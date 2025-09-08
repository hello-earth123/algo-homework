T = int(input())

for test_case in range(1, T+1):
    boxes = list(map(int, input().split()))
    # 만약 마지막 박스에 사탕이 1개밖에 없으면 만들 수 없음
    if boxes[2] == 1 or boxes[2] == 2 or boxes[1] == 1:
        is_increasing = False
    else:
        is_increasing = True

    eat = 0
    if is_increasing:
        while not (boxes[0] < boxes[1] < boxes[2]):
            while boxes[0] >= boxes[1]:
                boxes[0] -= 1
                eat += 1
            while boxes[1] >= boxes[2]:
                boxes[1] -= 1 
                eat += 1
    else:
        eat = -1

    print(f'#{test_case} {eat}')