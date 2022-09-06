def pascalsTriangle(rows):
    t = []
    for i in range(rows):
        t.append([])
        t[i].append(1)
        for j in range(1,i):
            t[i].append(t[i-1][j-1]+t[i-1][j])
        if i != 0:        
            t[i].append(1)
    return t

print(pascalsTriangle(5))

