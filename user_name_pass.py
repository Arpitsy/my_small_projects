a=input("WRITE YOUR USERNAME ")
b=input("WRITE YOUR PASSWROD")
c=any(d.isdigit() for d in b)
if len(a)>=5 and " " not in a  and len(b)>=8 and c:
    print("ACESS GRANTED")
else:

    if len(a)<5 or " " in a:

        print("Invalid Username")
    else:
        if len(b)<8 or c==False:
            print("Weak Password")
