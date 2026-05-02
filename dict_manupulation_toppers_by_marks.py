
mark={'a':28,'b':29,'c':78,'d':28,'e':87,'f':60,'h':28}
b=[i for i in mark.values()]
b.sort()
c=b[-1]
for i,j in mark.items():
    if j==c:
       print("These are the toppers",i)
h={}       
for i,j in mark.items():
    if j>40:
        h.update({i:j})
print(h)
unique=set(b)
print(unique)
