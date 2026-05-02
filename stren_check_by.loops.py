a=input("Write here")
d=a
b=0
for i in a :
    b+=1
c=any(d.isdigit() for d in a)    
if b>=8 and c and any(z in "@#$" for z in "@#$"):
    print("Strong Password")
else:
    print("Weak Password")
