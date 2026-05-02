a=input("Write here")
if len(a)%2==0:
    print(len(a)-1)
else:
    b=int(((len(a)+1)/2))
    print(a[b-1])
