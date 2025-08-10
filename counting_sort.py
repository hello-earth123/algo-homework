# def counting_sort(data, temp, k):
#     # data는 sort할 리스트 (0 이상, k 이하 정수)
#     # temp는 sort된 리스트
#     # counts는 카운트 배열
    
#     counts = [0] * k+1 # 실제 data[i]의 값을 count배열의 인덱스 실제 값에 넣기 때문
#     # data[x]가 만약 3이면 counts[3]에 +1을 한다는 뜻
    
#     # data[i]가 발생한 횟수를 counts 각 인덱스에 기록
#     for i in range(len(data)):
#         counts[data[i]] += 1
    
    
#     # counts 배열을 누적합으로 변경
#     for i in range(1, k+1):
#         counts[i] += counts[i-1]
        
    
#     # 뒤에서부터 순회하면서 그 숫자 뜨면 counts에서 하나 줄이고 그 누적합(누적합에서 하나 줄인 값)을 temp의 인덱스로 사용
#     for i in range(len(data)-1, -1 ,-1):
#         counts[data[i]] -= 1
#         temp[counts[data[i]]] = data[i]
        



# 여기서 k는 data의 최대값
def counting_sort(data, temp, k):
    
    counts = [0] * (k+1)
    for i in range(len(data)):
        counts[data[i]] += 1
        
        
    for i in range(1, k+1):
        counts[i] += counts[i-1]
        
    for i in range(len(data)-1, -1 ,-1):
        counts[data[i]] -= 1 
        temp[counts[data[i]]] = data[i]
        
        
def bubble_sort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


                
                


def counting_sort(data, temp, k):
    
    counts = [0] * (k+1)
    
    for i in range(len(data)):
        counts[data[i]] += 1
        
    for i in range(1, k+1):
        counts[i] += counts[i-1]
        
    for i in range(len(data)-1, -1, -1):
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]