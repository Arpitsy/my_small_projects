a=input("Write Here") 
b=0           
for i in range(1,int(a)+1):
    if int(a)==0:
        print("Not a prime no")
    else:
        if int(a)%i==0:
            b+=1
if b==2:
    print("its a prime no")
else:
    print("its not aprime no")
