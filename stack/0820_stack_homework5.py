def winner(p1, p2, cards):
    """두 학생 중 승자 인덱스를 반환"""
    a, b = cards[p1], cards[p2]

    # 같은 카드 → 번호 작은 학생이 승리
    if a == b:
        return p1
    # 가위(1)는 보(3) 이김, 바위(2)는 가위(1) 이김, 보(3)는 바위(2) 이김
    elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
        return p1
    else:
        return p2


def tournament(start, end, cards):
    """start ~ end 범위에서 최종 승자 인덱스를 반환"""
    if start == end:  # 한 명만 남았으면 그 학생이 승자
        return start

    mid = (start + end) // 2
    left = tournament(start, mid, cards)       # 왼쪽 그룹 승자
    right = tournament(mid + 1, end, cards)    # 오른쪽 그룹 승자

    return winner(left, right, cards)


# 실행 부분
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    result = tournament(0, N-1, cards)
    print(f"#{tc} {result+1}")  # 인덱스+1이 학생 번호
    