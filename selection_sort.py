def selection_sort(a, N):
    for i in range(N-1):    # 정렬 구간의 시작 인덱스
        min_idx = i         # 첫 원소를 최소로 가정
        for j in range(i+1, N):
            if a[min_idx] > a[j]: 
                min_idx = j         # 최소 원소 위치 갱신
        a[i], a[min_idx] = a[min_idx], a[i] # 구간 최솟값을 구간 맨 앞으로 
        
        
 
def selection_sort(a, N):
    # 버블 소트랑은 다르게 정 계단 모양이다. / 브루트포스 알고리즘이네
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N): # 구간을 전부 다 돌면서 제일 최소인 것을 찾는다.
            if a[min_idx] > a[j]:
                min_idx = j     # 구간 다 돌 때 까지 min_idx는 계속 업데이트 된다.
        a[min_idx], a[i] = a[i], a[min_idx] # 다 돌았으면 제일 최소인 것을 제일 앞으로 스왑한다.