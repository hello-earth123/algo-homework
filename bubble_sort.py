def bubble_sort(a, N): # N은 len(a)로 바꿔도 상관 없다.
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                
                

def bubble_sort(a, N):
    # 역 계단 모양 이거만 기억하자. 맨마지막 인덱스(0번 인덱스)는 비교 하는거 아니다. 알ㅏ서 자기 자리 찾아감
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
