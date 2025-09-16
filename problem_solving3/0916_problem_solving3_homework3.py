# 연산 우선순위 없음
# 결과 최대
from collections import deque
def bfs(number1, number2, cnt):
    queue = deque([(number1, number2, cnt)])
    visited = [-1] * 1000000001

    while queue:
        number1 + number2
        number1 - number2
        number1 * number2
        number1 / number2

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # + - * /
    operation = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    