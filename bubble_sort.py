def bubble_sort(a, N): # N은 len(a)로 바꿔도 상관 없다.
    for i in range(N-1, 1, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]