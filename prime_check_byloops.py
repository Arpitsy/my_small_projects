a=input("Write Here")
c=0
if int(a)==2:
        print("Its a Prime No")
elif int(a)<=1:
        print(" Not a Prime no")
else:
    for i in range(2,int(a),1):
        if int(a)%i==0:
            print("Its not a Prime no")
            break
    else:
        print("its a prime no")
              
