def bubble_sort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            
            
def selection_sort(a, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[min_idx], a[j] = a[j], a[min_idx]
        
        
def counting_sort(data, temp, k):
    counts = [0] * (k+1)
    
    for i in range(len(data)):
        counts[data[i]] += 1
        
    for i in range(1, k+1):
        counts[i] = counts[i-1]
        
    for i in range(len(data)-1, -1, -1):
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]