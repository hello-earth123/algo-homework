numbers = list(map(int, input().split()))

count = [0] * 1000001   
A = [0] * 1000000

# 카운트 배열 만들기
for i in range(len(numbers)):
    count[numbers[i]] += 1


# 누적합 만들기
for i in range(1, 1000000+1):
    count[i] += count[i-1]


# 역순으로 순회하면서 A 배열의 맞는 자리에 넣기
for i in range(len(numbers)-1, -1, -1):
    count[numbers[i]] -= 1

    A[count[numbers[i]]] = numbers[i]

print(A[500000])