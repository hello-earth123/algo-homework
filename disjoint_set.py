def make_set(n):
    parents = [i for i in range(n + 1)]
    return parents

def find_set(x):
    if x == parents[x]:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    global cnt
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return
    
    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y
    
parents = make_set(10)