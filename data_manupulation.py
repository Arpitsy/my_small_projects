data = [("a", 3), ("b", 1), ("c", 2)]

sort=[]
for i,j in data:
    sort.append(j)
sort.sort()
z=[]
for i in sort:
    for j,k in data:
        if i==k:
            z.append((j,k))
print(z)        
