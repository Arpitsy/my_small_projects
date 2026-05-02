a=input("WRITE HERE ")
b=len(a)
if b%2==0 and a[:int(b/2) ]==a[int(b/2):b]:
    print("Unique number")
else:
    print("Not unique")
