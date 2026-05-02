a=int(input("Write your FIrst no Here"))
b=input("WRITE OPERAION \n + \n -\n *\n /")
c=int(input("Write the 2nd no here"))
if b=="+" :
    d=(a+c)
    print(d,end=" ")
    if d>=100:
        print("YR ANS IS BIG")
    elif d<0:
        print("YR NAS IS -VE")
elif b=="-":
    e=int((a-c))
    print(e,end=" ")
    if e>=100:
        print("ITS A BIG ANS")
    elif e<0:
        print("YR NO IS -VE")
elif b=="*":
    f=int((a*c))
    print(f, end=" ")
    if f>=100:
        print("YR ANS IS BIG")
    elif f<0 :
        print("YR AND IS -VE")
elif b=="/":
    z=(456)
    if c==0:
        print("INVALID NO")
    else:
        h = (a/c)
        print(h,end=" ")
        if h>=100:
         print("YR NO IS BIG")
        elif h<0:
         print("YR NO IS -VE")
